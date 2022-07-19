from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk
import os

os.system("Xvfb :1 -screen 0 720x720x16 &")
os.environ['DISPLAY'] = ":1.0"

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='C:\\Users\\Mama Modiselle\\Pictures\\example', title='Select Image')
