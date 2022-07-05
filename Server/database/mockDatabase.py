import bcrypt
from dotenv import load_dotenv
import psycopg2.extras
import psycopg2
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

load_dotenv()

class mockDatabase:
    """
    Constructor:
        Connects to the database.
    Parameters:
        None
    Returns:
        Boolean:Returns false if database connection fails
    """

    db_list = None
    db_id = None
    db_history = None
    db_history_id = None
    db_feedback = None
    def __init__(self):
        self.db_list = []
        self.db_history = []
        self.db_feedback = []
        self.db_id = 1
        self.db_history_id = 1
        self.db_feedback_id = 1
        print("Database connection successful")

    def register(self, name, surnname, email, password):
        if self.getUserWithEmail(email) == None:
            encoded_password = bytes(password, encoding='utf-8')
            encrypted_password = bcrypt.hashpw(
                encoded_password, bcrypt.gensalt())
            # print(type(encrypted_password))
            encrypted_password = encrypted_password.decode('UTF-8')
            code = '1111'
            user_id = self.db_id
            self.db_id += 1

            user = [user_id,name, surnname,
                    encrypted_password, email]
            self.db_list.append(user)
            return True
        else:
            return False

    def login(self, email, password):
        user = self.getUserWithEmail(email)
        if user != None:
            if bcrypt.checkpw(password.encode('UTF-8'), user[3].encode('UTF-8')):
                #print("password works")
                return True
            else:
                return False
        return False

    def getUserWithEmail(self, email):
        for x in self.db_list:
            if x[4] == email:
                return x
        return None

    def getUserWithId(self, id):
        for x in self.db_list:
            if x[0] == id:
                return x
        return None


    def insert_image(self, image_uploaded,image_converted, id):
        if self.getUserWithId(id) != None:
            history_id = self.db_history_id
            self.db_history_id += 1
            hist = [history_id,'straigh line', id,
                        image_uploaded, image_converted]
            self.db_history.append(hist)
            return True
        else:
            return False
    
    def get_image(self, id):
        for x in reversed(self.db_history) :
            if x[2] == id:
                return x
        return None

    #fetches previously uploaded images
    def get_image_history(self, id):
        temp_list = []
        for x in reversed(self.db_history):
            if x[2] == id:
                temp_list.append(x)
        
        return temp_list

    def delete_history(self,id):
        for x in reversed(self.db_history):
            if x[0] == id:
                self.db_history.remove(x)
                return True
        return False

    def insert_feedback(self, id, feedback):
        if self.getUserWithId(id) != None:
            feed_id = self.db_feedback_id
            self.db_feedback_id += 1
            hist = [feed_id, id,feedback]
            self.db_history.append(hist)
            return True
        else:
            return False