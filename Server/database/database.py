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

    """
    __init__ function:
        initialises the database connection
    Parameters: 
        self (current instance)
    Returns: 
        prints out success string if database connection is successful
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

    """
         register function:
            registers a new user and adds user to the database
        Parameters: 
            self (current instance), the name,  surname, email, & password for each user
        Returns: 
            True or False, depending on whether the regustration was successful or not
            also prints an error message if registration was unsuccessful
    """

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


    """
         login function:
            checks the parameters to verify whether a user exists in the database to allow for the user to login to the system
        Parameters: 
            self (current instance), the email, & password for each user
        Returns: 
            True or False, depending on whether the regustration was successful or not
            also prints an error message if login was unsuccessful
    """

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

    """
         getUserWithEmail function:
            verifies whether the user exists on the database, using the user's email
        Parameters: 
            self (current instance) & the email for each user
        Returns: 
            db_user which is the sql statement needed to verify the user   
    """
    def getUserWithEmail(self, email):
        sql = "SELECT * FROM users where email=%s;"
        self.cur.execute(sql, (email,))
        db_user = self.cur.fetchone()
        self.conn.commit()
        return db_user

    """
         insert_image function:
            inserts the uploaded image together with its converted image for the user's upload history
        Parameters: 
            self (current instance) & the uploaded image and the converted image for each user
        Returns: 
            True or False, depending on whether the image insertion was successful or not   
    """

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
    
    """
         get_image function:
            retrieves an uploaded image using a valid id 
        Parameters: 
            self (current instance) & user id
        Returns: 
            db_history if retrieval was successful & False if it was unsuccessful
            also prints an error message if it was unsuccessful  
    """

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

    
    """
         get_image function:
            retrieves previously uploaded images
        Parameters: 
            self (current instance) & user id
        Returns: 
            db_history if retrieval was successful & False if it was unsuccessful
            also prints an error message if it was unsuccessful  
    """
    def get_image_history(self, id):
        try:
            sql = "SELECT * FROM history where user_id=%s ORDER BY id DESC"
            self.cur.execute(sql, ([id]))
            db_history = self.cur.fetchmany(6)
            self.conn.commit()
            return db_history
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    """
         delete_history function:
            deletes selected images from the history table for a specific user
        Parameters: 
            self (current instance) & user id
        Returns: 
            True or False, depending on whether the deletion was successful or not  
    """
    def delete_history(self,id):
        try:
            sql = "DELETE FROM history WHERE id=%s;"
            self.cur.execute(sql, ([id]))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    """
         insert_feedback function:
            inserts the user feedback from the form into the feedback table in the database
        Parameters: 
            self (current instance), user id & feedback
        Returns: 
            True or False, depending on whether the insertion was successful or not  
    """

    def insert_feedback(self, id, feedback):
        try:
            sql = "INSERT INTO feedback (user_id,feedback) VALUES(%s,%s)"
            self.cur.execute(sql, (id, feedback))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False