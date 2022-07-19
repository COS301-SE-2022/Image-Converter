import cv2
import tensorflow as tf

img_pred =[]
test_image = '..\\assets\\bargraph.png'
##################################################################################
## Pie vs Line
##################################################################################

CATEGORIES = ["pie_chart", "line_graph"]

def prepare(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
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
    print("Image is a line graph")
elif((img_pred.count("pie_chart") ==2)):
    print("Image is a pie chart")
