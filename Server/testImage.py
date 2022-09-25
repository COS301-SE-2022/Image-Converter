import urllib.request
import uuid
from PIL import Image

myUUID = str(uuid.uuid4())
urllib.request.urlretrieve(
'https://storage.googleapis.com/hardcode-9aba7.appspot.com/2.jpg?Expires=1688845990&GoogleAccessId=firebase-adminsdk-fdx52%40hardcode-9aba7.iam.gserviceaccount.com&Signature=jcwVz3VFr3gf8fdgqSgAeQolUJ%2Fv9ob72V6clqL%2FVY1TV9mwgGCiVIQsAPuZT1gxyhGM%2BiYlSmfyIAq0%2FDyGWXzs%2Bqz9SKnLAE0PN0tBTVLk2Y9hYBH7HZn7nRRYupkYnBKFJ6i7c%2F5croBnucj8ALjbVh3zGszhz%2B4YPY%2FODwIoqX9vF5AilU7vd09a4%2BMfYBKMldqvYIA%2FxNIpLeP2aKKGri5%2FdBQv1Jxkn%2FeGKshMPoBt8bWdcI9ixBte13hiXz8%2FCkGSY6cT2wUJpbDIFo36v75KeCHj96c3Y%2BrV%2FbNydiRXwd9kIDetwuegY2Nz2toxJeUZ2drG2d3DcM%2Br0g%3D%3D',
myUUID+"img.png")




print(f"UUID/GUID -> {myUUID}")
img = Image.open("img.png")
img.show()
