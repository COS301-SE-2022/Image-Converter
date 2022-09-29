import argparse
import cv2
import glob
import math
import numpy as np
import os
import torch
from basicsr.archs.rrdbnet_arch import RRDBNet
# from torch.nn import functional as F


def main():
    model_path = 'RealESRGAN_x4plus.pth'
    img_path = '/Users/neoseefane/Documents/GitHub/Image-Converter/Server/converter/draw.jpeg'
    # /Users/neoseefane/Documents/GitHub/Image-Converter/Server/converter/Graph.png
    # converter/barGraph.jpeg
    # plottedGraph.png
    #hr_images/hrbar_chart_image12 (2).png.jpg
    # device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
    # initialize model
    if torch.backends.mps.is_available():
        device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
    else:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32)
    loadnet = torch.load(model_path)
    if 'params_ema' in loadnet:
        keyname = 'params_ema'
    else:
        keyname = 'params'
    model.load_state_dict(loadnet[keyname], strict=True)
    model.eval()
    model = model.to(device)
    print('Model path {:s}. \nTesting...'.format(model_path))

    # img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED).astype(np.float32)
    img = cv2.imread(img_path,  cv2.IMREAD_UNCHANGED).astype(np.float32)
    # cv2.imshow("Image: ", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    os.makedirs('results/', exist_ok=True)

    if np.max(img) > 255:  # 16-bit image
        max_range = 65535
        print('\tInput is a 16-bit image')
    else:
        max_range = 255
    img = img / max_range
    if len(img.shape) == 2:  # gray image
        img_mode = 'L'
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    elif img.shape[2] == 4:  # RGBA image with alpha channel
        img_mode = 'RGBA'
        alpha = img[:, :, 3]
        img = img[:, :, 0:3]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # if args.alpha_upsampler == 'realesrgan':
        #     alpha = cv2.cvtColor(alpha, cv2.COLOR_GRAY2RGB)
    else:
        img_mode = 'RGB'
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img1 = img
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img = img.unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(img).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = output[:, :, ::-1].copy()
    print(output.shape)
    # output = (output * 255.0).round()
    # upsampler
    # cv2.imshow("Image: ", output)
    # cv2.imshow("Image2: ", img1[:, :, ::-1].copy())
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# class RealESRGANer():
#
#     def __init__(self, scale, model_path, tile=0, tile_pad=10, pre_pad=10):
#         self.scale = scale
#         self.tile_size = tile
#         self.tile_pad = tile_pad
#         self.pre_pad = pre_pad
#         self.mod_scale = None
#
#         # initialize model
#         if torch.backends.mps.is_available():
#             self.device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
#         else:
#             self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#         # self.device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
#         model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32)
#         loadnet = torch.load(model_path)
#         if 'params_ema' in loadnet:
#             keyname = 'params_ema'
#         else:
#             keyname = 'params'
#         model.load_state_dict(loadnet[keyname], strict=True)
#         model.eval()
#         self.model = model.to(self.device)
#
#     def pre_process(self, img):
#         img = torch.from_numpy(np.transpose(img, (2, 0, 1))).float()
#         self.img = img.unsqueeze(0).to(self.device)
#
#         # pre_pad
#         if self.pre_pad != 0:
#             self.img = F.pad(self.img, (0, self.pre_pad, 0, self.pre_pad), 'reflect')
#         # mod pad
#         if self.scale == 2:
#             self.mod_scale = 2
#         elif self.scale == 1:
#             self.mod_scale = 4
#         if self.mod_scale is not None:
#             self.mod_pad_h, self.mod_pad_w = 0, 0
#             _, _, h, w = self.img.size()
#             if (h % self.mod_scale != 0):
#                 self.mod_pad_h = (self.mod_scale - h % self.mod_scale)
#             if (w % self.mod_scale != 0):
#                 self.mod_pad_w = (self.mod_scale - w % self.mod_scale)
#             self.img = F.pad(self.img, (0, self.mod_pad_w, 0, self.mod_pad_h), 'reflect')
#
#     def process(self):
#         try:
#             # inference
#             with torch.no_grad():
#                 self.output = self.model(self.img)
#         except Exception as error:
#             print('Error', error)
#
#     def tile_process(self):
#         """Modified from: https://github.com/ata4/esrgan-launcher
#         """
#         batch, channel, height, width = self.img.shape
#         output_height = height * self.scale
#         output_width = width * self.scale
#         output_shape = (batch, channel, output_height, output_width)
#
#         # start with black image
#         self.output = self.img.new_zeros(output_shape)
#         tiles_x = math.ceil(width / self.tile_size)
#         tiles_y = math.ceil(height / self.tile_size)
#
#         # loop over all tiles
#         for y in range(tiles_y):
#             for x in range(tiles_x):
#                 # extract tile from input image
#                 ofs_x = x * self.tile_size
#                 ofs_y = y * self.tile_size
#                 # input tile area on total image
#                 input_start_x = ofs_x
#                 input_end_x = min(ofs_x + self.tile_size, width)
#                 input_start_y = ofs_y
#                 input_end_y = min(ofs_y + self.tile_size, height)
#
#                 # input tile area on total image with padding
#                 input_start_x_pad = max(input_start_x - self.tile_pad, 0)
#                 input_end_x_pad = min(input_end_x + self.tile_pad, width)
#                 input_start_y_pad = max(input_start_y - self.tile_pad, 0)
#                 input_end_y_pad = min(input_end_y + self.tile_pad, height)
#
#                 # input tile dimensions
#                 input_tile_width = input_end_x - input_start_x
#                 input_tile_height = input_end_y - input_start_y
#                 tile_idx = y * tiles_x + x + 1
#                 input_tile = self.img[:, :, input_start_y_pad:input_end_y_pad, input_start_x_pad:input_end_x_pad]
#
#                 # upscale tile
#                 try:
#                     with torch.no_grad():
#                         output_tile = self.model(input_tile)
#                 except Exception as error:
#                     print('Error', error)
#                 print(f'\tTile {tile_idx}/{tiles_x * tiles_y}')
#
#                 # output tile area on total image
#                 output_start_x = input_start_x * self.scale
#                 output_end_x = input_end_x * self.scale
#                 output_start_y = input_start_y * self.scale
#                 output_end_y = input_end_y * self.scale
#
#                 # output tile area without padding
#                 output_start_x_tile = (input_start_x - input_start_x_pad) * self.scale
#                 output_end_x_tile = output_start_x_tile + input_tile_width * self.scale
#                 output_start_y_tile = (input_start_y - input_start_y_pad) * self.scale
#                 output_end_y_tile = output_start_y_tile + input_tile_height * self.scale
#
#                 # put tile into output image
#                 self.output[:, :, output_start_y:output_end_y,
#                             output_start_x:output_end_x] = output_tile[:, :, output_start_y_tile:output_end_y_tile,
#                                                                        output_start_x_tile:output_end_x_tile]
#
#     def post_process(self):
#         # remove extra pad
#         if self.mod_scale is not None:
#             _, _, h, w = self.output.size()
#             self.output = self.output[:, :, 0:h - self.mod_pad_h * self.scale, 0:w - self.mod_pad_w * self.scale]
#         # remove prepad
#         if self.pre_pad != 0:
#             _, _, h, w = self.output.size()
#             self.output = self.output[:, :, 0:h - self.pre_pad * self.scale, 0:w - self.pre_pad * self.scale]
#         return self.output


if __name__ == '__main__':
    main()
    # model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
    # netscale = 4
    # model_path = '/Users/neoseefane/Documents/GitHub/Image-Converter/Server/converter/imageSmoothing/RealESRGAN_x4plus.pth'
    # img_path = '/Users/neoseefane/Documents/GitHub/Image-Converter/Server/converter/imageSmoothing/download.png'
    # img = cv2.imread(img_path)
    # obj = RealESRGANer(netscale, model_path)
    # obj.pre_process(img)
    # obj.process()
    # output = obj.post_process()
    # cv2.imshow('RealESRGAN output', output)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

