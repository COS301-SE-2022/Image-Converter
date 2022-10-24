from PIL import Image
import operator
from collections import deque
from io import StringIO
import timeit

class SVG:
    def __init__(self, path):
        self.path = path
        self.img = Image.open(self.path).convert('RGBA')
      
        start = timeit.timeit()
        self.svgImg = self.rgba_image_to_svg_contiguous(self.img)
        end = timeit.timeit()
        print(end - start)
        with open("examples/angular.svg", "w") as text_file:
            text_file.write(self.svgImg)

    def add_tuple(self, a, b):
        return tuple(map(operator.add, a, b))

    def sub_tuple(self, a, b):
        return tuple(map(operator.sub, a, b))

    def neg_tuple(self,a):
        return tuple(map(operator.neg, a))

    def direction(self, edge):
        return self.sub_tuple(edge[1], edge[0])

    def magnitude(self, a):
        return int(pow(pow(a[0], 2) + pow(a[1], 2), .5))

    def normalize(self, a):
        mag = self.magnitude(a)
        assert mag > 0, "Cannot normalize a zero-length vector"
        return tuple(map(operator.truediv, a, [mag]*len(a)))

    def svg_header(self, width, height):
        return """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
    "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <svg width="%d" height="%d"
        xmlns="http://www.w3.org/2000/svg" version="1.1">
    """ % (width, height)    

    def joined_edges(self, assorted_edges, keep_every_point=False):
        pieces = []
        piece = []
        directions = deque([
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            ])
        while assorted_edges:
            if not piece:
                piece.append(assorted_edges.pop())
            current_direction = self.normalize(self.direction(piece[-1]))
            while current_direction != directions[2]:
                directions.rotate()
            for i in range(1, 4):
                next_end = self.add_tuple(piece[-1][1], directions[i])
                next_edge = (piece[-1][1], next_end)
                if next_edge in assorted_edges:
                    assorted_edges.remove(next_edge)
                    if i == 2 and not keep_every_point:
                        # same direction
                        piece[-1] = (piece[-1][0], next_edge[1])
                    else:
                        piece.append(next_edge)
                    if piece[0][0] == piece[-1][1]:
                        if not keep_every_point and self.normalize(self.direction(piece[0])) == self.normalize(self.direction(piece[-1])):
                            piece[-1] = (piece[-1][0], piece.pop(0)[1])
                            # same direction
                        pieces.append(piece)
                        piece = []
                    break
            else:
                raise Exception ("Failed to find connecting edge")
        return pieces

    def rgba_image_to_svg_contiguous(self, im, opaque=None, keep_every_point=False):

        # collect contiguous pixel groups
        
        adjacent = ((1, 0), (0, 1), (-1, 0), (0, -1))
        visited = Image.new("1", im.size, 0)
        
        color_pixel_lists = {}

        width, height = im.size
        for x in range(width):
            for y in range(height):
                here = (x, y)
                if visited.getpixel(here):
                    continue
                rgba = im.getpixel((x, y))
                if opaque and not rgba[3]:
                    continue
                piece = []
                queue = [here]
                visited.putpixel(here, 1)
                while queue:
                    here = queue.pop()
                    for offset in adjacent:
                        neighbour = self.add_tuple(here, offset)
                        if not (0 <= neighbour[0] < width) or not (0 <= neighbour[1] < height):
                            continue
                        if visited.getpixel(neighbour):
                            continue
                        neighbour_rgba = im.getpixel(neighbour)
                        if neighbour_rgba != rgba:
                            continue
                        queue.append(neighbour)
                        visited.putpixel(neighbour, 1)
                    piece.append(here)

                if not rgba in color_pixel_lists:
                    color_pixel_lists[rgba] = []
                color_pixel_lists[rgba].append(piece)

        del adjacent
        del visited

        # calculate clockwise edges of pixel groups

        edges = {
            (-1, 0):((0, 0), (0, 1)),
            (0, 1):((0, 1), (1, 1)),
            (1, 0):((1, 1), (1, 0)),
            (0, -1):((1, 0), (0, 0)),
            }
                
        color_edge_lists = {}

        for rgba, pieces in color_pixel_lists.items():
            for piece_pixel_list in pieces:
                edge_set = set([])
                for coord in piece_pixel_list:
                    for offset, (start_offset, end_offset) in edges.items():
                        neighbour = self.add_tuple(coord, offset)
                        start = self.add_tuple(coord, start_offset)
                        end = self.add_tuple(coord, end_offset)
                        edge = (start, end)
                        if neighbour in piece_pixel_list:
                            continue
                        edge_set.add(edge)
                if not rgba in color_edge_lists:
                    color_edge_lists[rgba] = []
                color_edge_lists[rgba].append(edge_set)

        del color_pixel_lists
        del edges

        # join edges of pixel groups

        color_joined_pieces = {}

        for color, pieces in color_edge_lists.items():
            color_joined_pieces[color] = []
            for assorted_edges in pieces:
                color_joined_pieces[color].append(self.joined_edges(assorted_edges, keep_every_point))

        s = StringIO()
        s.write(self.svg_header(*im.size))

        for color, shapes in color_joined_pieces.items():
            for shape in shapes:
                s.write(""" <path d=" """)
                for sub_shape in shape:
                    here = sub_shape.pop(0)[0]
                    s.write(""" M %d,%d """ % here)
                    for edge in sub_shape:
                        here = edge[0]
                        s.write(""" L %d,%d """ % here)
                    s.write(""" Z """)
                s.write(""" " style="fill:rgb%s; fill-opacity:%.3f; stroke:none;" />\n""" % (color[0:3], float(color[3]) / 255))
                
        s.write("""</svg>\n""")
        return s.getvalue()

    def rgba_image_to_svg_pixels(self, im, opaque=None):
        s = StringIO()
        s.write(self.svg_header(*im.size))

        width, height = im.size
        for x in range(width):
            for y in range(height):
                here = (x, y)
                rgba = im.getpixel(here)
                if opaque and not rgba[3]:
                    continue
                s.write("""  <rect x="%d" y="%d" width="1" height="1" style="fill:rgb%s; fill-opacity:%.3f; stroke:none;" />\n""" % (x, y, rgba[0:3], float(rgba[2]) / 255))
        s.write("""</svg>\n""")
        return s.getvalue()

    def main(self):
        image = Image.open('/Users/neoseefane/Documents/GitHub/Image-Converter/Server/converter/draw.jpeg').convert('RGBA')
        svg_image = self.rgba_image_to_svg_contiguous(image)
        #svg_image = rgba_image_to_svg_pixels(image)
        with open("examples/angular.svg", "w") as text_file:
            text_file.write(svg_image)

if __name__ == '__main__':
    SVG('charts.png')
   
  
    