import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
import re
from PIL import Image
from pytesseract import pytesseract
import base64

class NLPTags:
    def __init__(self,uploaded_image):
        sliced_png = uploaded_image[22:]

        converted_base64= bytes(sliced_png, encoding='utf8')
        with open("img2.png", "wb") as fh:
            fh.write((base64.decodebytes(converted_base64)))
        self.uploaded_image = 'img2.png'
        self.graphType = ""
        self.extract()



    def extract(self):

      ############################################################################################################
      ######################################  Initialization  ####################################################
      ############################################################################################################

      # Download tesseract using link
      # https://github.com/UB-Mannheim/tesseract/wiki

      #Define path to tessaract.exe
      path_to_tesseract = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')

      #Define path to image
      path_to_image = self.uploaded_image

      #Point tessaract_cmd to tessaract.exe
      pytesseract.tesseract_cmd = path_to_tesseract

      #Open image with PIL
      img = Image.open(path_to_image)

      #Extract text from image
      text = pytesseract.image_to_string(img)

      # print(text)

      ############################################################################################################
      ######################################  Processing  ########################################################
      ############################################################################################################

      # Uncomment this section for running first time
      ############################################################################################################
      # nltk.download('stopwords')
      # nltk.download('punkt')
      # nltk.download('words')
      ############################################################################################################

      #Convert text to lowercase
      text_lowercase = text.lower()

      #Remove numbers
      text_no_num = ''.join(c for c in text_lowercase if not c.isdigit())

      #Remove characters less than lenght 2
      text_under_two = re.sub(r'\b\w{1,2}\b', '', text_no_num)

      #Remove punctuation and special characters
      tokenizer = RegexpTokenizer(r'\w+')   

      #Tokenize text
      tokens = tokenizer.tokenize(text_under_two)
      print(tokens)

      #Remove non english words
      self.dict_words= []
      #Mieliestronk dictionary
      with open("dictionary.txt", "r") as a_file:
        for line in a_file:
          stripped_line = line.strip()
          for n in tokens:
              if n == stripped_line:
                  self.dict_words.append(n)

      #Remove stop words
      tokens_no_stop = [word for word in self.dict_words if not word in stopwords.words()]

      #Removing duplicate words
      final_tokens = list(set(tokens_no_stop))

      print(final_tokens)
      return self.dict_words