import bcrypt
from dotenv import load_dotenv
import psycopg2.extras
import psycopg2
import os
import sys
from database.firebase import FireStore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore,storage
import cv2
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

load_dotenv()

cred = credentials.Certificate("database/firebaseKey.json")
firebase_admin.initialize_app(cred,{'storageBucket': os.environ.get('BUCKET_NAME')})

class User:
    """
    Constructor:
        Connects to the database.
    Parameters:
        None
    Returns:
        Boolean:Returns false if database connection fails
    """

    def __init__(self):
        try:
            self.DB_HOST = os.environ.get('DB_HOST')
            self.DB_NAME = os.environ.get('DB_NAME')
            self.DB_PASS = os.environ.get('DB_PASS')
            self.DB_USER = os.environ.get('DB_USER')
            self.conn = psycopg2.connect(
                dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS, host=self.DB_HOST)
            self.cur = self.conn.cursor()
            print("Database connection successful")
        except:
            return None

    def register(self, name, surname, email, password):
        try:
            encoded_password = bytes(password, encoding='utf-8')
            encrypted_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            encrypted_password = encrypted_password.decode('UTF-8')
            

            sql = "INSERT INTO users (name,surname,password,email) VALUES(%s,%s,%s,%s)"
            self.cur.execute(sql, (name, surname, encrypted_password, email))
            self.conn.commit()
            
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    def login(self, email, password):
        try:
            sql = "SELECT password FROM users where email=%s;"
            self.cur.execute(sql, (email,))
            db_password = self.cur.fetchone()
            self.conn.commit()
            if db_password != None:
                if bcrypt.checkpw(password.encode('UTF-8'), db_password[0].encode('UTF-8')):
                    return True
                else:
                    return False
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    def getUserWithEmail(self, email):
        sql = "SELECT * FROM users where email=%s;"
        self.cur.execute(sql, (email,))
        db_user = self.cur.fetchone()
        self.conn.commit()
        return db_user

    def countRows(self):
        try:
            sql = "SELECT count(*) FROM history2;"
            self.cur.execute(sql)
            db_count = self.cur.fetchone()
            self.conn.commit()
            print(db_count[0])
            return db_count
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    def insert_image(self, image_uploaded,image_converted, id,graphType):
        try: 
            
            value = self.countRows()
            count = value[0] + 1
            print("here")
            print(count)
            cv2.imwrite("images/original/Original.png", image_uploaded)
            cv2.imwrite("images/original/Converted.png", image_converted)
            fireStore1 = FireStore()
            link=fireStore1.uploadImage("images/original/Original.png",str(count)+"Original.jpg")
            link2=fireStore1.uploadImage("images/original/Converted.png",str(count)+"Converted.jpg")
            # print(link)
            print("Converted ")
            # print(link2)
            #sql = "INSERT INTO history (graph_type,user_id,image_uploaded,image_converted) VALUES(%s,%s,%s,%s)"
            sql = "INSERT INTO history2 (graph_type,user_id,image_uploaded,image_converted) VALUES(%s,%s,%s,%s)"
            print("Executing")
            self.cur.execute(sql, (graphType, id, link,link2))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
    
    def get_image(self, id):
        try:
            #sql = "SELECT * FROM history where user_id=%s;"
            sql = "SELECT * FROM history2 where user_id=%s ORDER BY id DESC LIMIT 1;"
            self.cur.execute(sql, ([id]))
            db_history = self.cur.fetchone()
            self.conn.commit()
            # print(db_history)
            return db_history
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    #fetches previously uploaded images
    def get_image_history(self, id):
        try:
            sql = "SELECT * FROM history2 where user_id=%s ORDER BY id DESC"
            self.cur.execute(sql, ([id]))
            db_history = self.cur.fetchmany(6)
            self.conn.commit()
            return db_history
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    
    def getUnrecognizedImages(self):
        try:
            sql = "SELECT * FROM history2 where graph_type=%s ORDER BY id DESC"
            graphType="unrecognized"
            self.cur.execute(sql,([graphType]))
            db_history = self.cur.fetchmany(6)
            self.conn.commit()
            print("Unrecognized")
            return db_history
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    

    def delete_history(self,id):
        try:
            sql = "DELETE FROM history2 WHERE id=%s;"
            self.cur.execute(sql, ([id]))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    def insert_feedback(self, id, feedback):
        try:
            sql = "INSERT INTO feedback (user_id,feedback) VALUES(%s,%s)"
            self.cur.execute(sql, (id, feedback))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
            
    def insert_code(self, email, code):
        try:
            sql = "INSERT INTO code (email,code) VALUES(%s,%s)"
            self.cur.execute(sql, (email, code))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
            
    def updatePassword(self, email, password):
        try:
            encoded_password = bytes(password, encoding='utf-8')
            encrypted_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            encrypted_password = encrypted_password.decode('UTF-8')
            
            sql = "UPDATE users SET password =%s WHERE email= %s;"
            self.cur.execute(sql, (encrypted_password, email))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
    
    def get_code(self, email):
        try:
            #sql = "SELECT * FROM history where user_id=%s;"
            sql = "SELECT * FROM code where email=%s ORDER BY id DESC LIMIT 1;"
            self.cur.execute(sql, ([email]))
            code = self.cur.fetchone()
            self.conn.commit()
            # print(db_history)
            return code
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
    
    def updateGraphType(self, graphType,id):
        try:
            sql = "UPDATE history2 SET graph_type =%s WHERE id= %s;"
            self.cur.execute(sql, (graphType, id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
    

    def deleteUnrecognizedImages(self, id):
        try:
            sql = "DELETE FROM history2 WHERE id=%s;"
            self.cur.execute(sql, ([id]))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    def incrementActivity(self,activity):
        try:
            sql ="UPDATE tracking SET count =count + 1 WHERE activity= %s;"
            self.cur.execute(sql, (activity,))
            self.conn.commit()
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    def decrementActivity(self,activity):
        try:
            sql ="UPDATE tracking SET count =count - 1 WHERE activity= %s;"
            self.cur.execute(sql, (activity,))
            self.conn.commit()
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    def getActivities(self):
        try:
            sql = "SELECT * FROM tracking FETCH FIRST 3 ROW ONLY;"
            self.cur.execute(sql,)
            code = self.cur.fetchall()
            self.conn.commit()
            return code
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

if __name__ == "__main__":
    db=User()
    print(db.getActivities()[0][1])
    # db.incrementActivity("Uploads")
    # db.incrementActivity("Downloads")
    # db.incrementActivity("Unrecognized")
    # db.register("test", "test", "u19081082@tuks.co.za", "test")