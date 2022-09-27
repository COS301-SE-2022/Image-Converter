
import datetime
# from msilib.schema import Class
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore,storage
import sys
import numpy as np
import cv2
import os

load_dotenv()

class FireStore:
    def __init__(self):
        try:
            config={
                "type": "service_account",
                "project_id": os.environ.get('PROJECT_ID'),
                "private_key_id": os.environ.get('PRIVATE_KEY_ID'),
                "private_key": os.environ.get('PRIVATE_KEY'),
                "client_email": os.environ.get('CLIENT_EMAIL'),
                "client_id": os.environ.get('CLIENT_ID'),
                "auth_uri": os.environ.get('AUTH_URI'),
                "token_uri": os.environ.get('TOKEN_URI'),
                "auth_provider_x509_cert_url": os.environ.get('AUTH_PROVIDER_x509_CERT_URL'),
                "client_x509_cert_url": os.environ.get('CLIENT_x509_CERT_URL')
            }
            cred = credentials.Certificate(config)
            firebase_admin.initialize_app(cred,{'storageBucket': os.environ.get('BUCKET_NAME')})
            db=firestore.client()
            
            print("Firebase connection successful")
        except:
            return None
    
    def uploadImage(self,image,name):
        try:
            
            bucket = storage.bucket()
            blob = bucket.blob(name)
            blob.upload_from_filename(image)
            pic = bucket.get_blob(name).generate_signed_url(datetime.timedelta(days=365),method='GET')
            # print(pic)
            return pic
        except Exception as e:
            print(f"Firebase error: {e}")
            return None
    # db=firestore.client()

    # db.collection('persons').add({'name':'lee','Age':20})

    # bucket = storage.bucket()
    # bucket.blob('test.jpg').upload_from_filename('test.jpg')
    
    # arr = np.frombuffer(blob.download_as_string(), np.uint8)
    # img = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)

    # cv2.imshow('image',img)
    # cv2.waitKey(0)

#create main to test the class
if __name__ == "__main__":
    fireStore1 = FireStore()
    link=fireStore1.uploadImage("TreeDiagram.jpg","1.jpg")
    print(link)
    