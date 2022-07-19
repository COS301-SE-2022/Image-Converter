from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk
import os


root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='C:\\Users\\Mama Modiselle\\Pictures\\example', title='Select Image')
