import cv2
import tensorflow as tf

"""
img_pred =[]
test_image = '..\\assets\\bargraph.png'

##################################################################################
## Pie vs Line
##################################################################################

CATEGORIES = ["pie_chart", "line_graph"]

def prepare(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    print("|-------|")
    print((filepath))
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    print("|-------|")
    print((img_array))
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model('Pie_v_Line-CNN.model')

prediction = model.predict([prepare(test_image)])

img_pred.append(CATEGORIES[int(prediction[0][0])])


##################################################################################
## Pie vs Bar
##################################################################################


CATEGORIES2 = ["pie_chart", "bar_chart"]

def prepare(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model('Pie_v_Bar-CNN.model')

prediction = model.predict([prepare(test_image)])

img_pred.append(CATEGORIES2[int(prediction[0][0])])

##################################################################################
## Bar vs Line
##################################################################################


CATEGORIES3 = ["bar_chart", "line_graph"]

def prepare(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model('Bar_v_Line-CNN.model')

prediction = model.predict([prepare(test_image)])

img_pred.append(CATEGORIES3[int(prediction[0][0])])

print(img_pred)

if(img_pred.count("bar_chart") ==2):
    print("Image is a bar chart")
elif((img_pred.count("line_graph") ==2)):
    print("Image is a line_graph")
elif((img_pred.count("pie_chart") ==2)):
    print("Image is a pie chart")

"""


img_pred =[]

base64img = b'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'
import base64
with open("img.png", "wb") as fh:
    fh.write(base64.decodebytes(base64img))

test_image = 'img.png' 

CATEGORIES = ["pie_chart", "line_graph"]

def prepare(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model('Pie_v_Line-CNN.model')

prediction = model.predict([prepare(test_image)])

img_pred.append(CATEGORIES[int(prediction[0][0])])

print(img_pred)