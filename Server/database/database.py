import bcrypt
from dotenv import load_dotenv
import psycopg2.extras
import psycopg2
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

load_dotenv()

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
            # print(encrypted_password)
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

    def insert_image(self, image_uploaded,image_converted, id):
        try: 
            #sql = "INSERT INTO history (graph_type,user_id,image_uploaded,image_converted) VALUES(%s,%s,%s,%s)"
            sql = "INSERT INTO history (graph_type,user_id,image_uploaded,image_converted) VALUES(%s,%s,%s,%s)"
            print("Executing")
            self.cur.execute(sql, ('straight line', id, image_uploaded,image_converted))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
    
    def get_image(self, id):
        try:
            #sql = "SELECT * FROM history where user_id=%s;"
            sql = "SELECT * FROM history where user_id=%s ORDER BY id DESC LIMIT 1;"
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
            sql = "SELECT * FROM history where user_id=%s;"
            self.cur.execute(sql, ([id]))
            db_history = self.cur.fetchall()
            self.conn.commit()
            # print("hist: ",db_history)
            # print("len: ",len(db_history))
            # print("hist: ",db_history[0][4])
            return db_history
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    def delete_history(self,id):
        try:
            sql = "DELETE FROM history WHERE id=%s;"
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
            