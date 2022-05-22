import bcrypt
import random
from flask import request, json
from dotenv import load_dotenv
import psycopg2.extras
import psycopg2
from flask import Flask
from database.send_email import Email
import os
import sys
import functools
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
        except:
            return None

    def register(self, name, surname, password, email):
        try:
            encoded_password = bytes(password, encoding='utf-8')
            encrypted_password = bcrypt.hashpw(
                encoded_password, bcrypt.gensalt())
            # print(type(encrypted_password))
            encrypted_password = encrypted_password.decode('UTF-8')
            sql = "INSERT INTO users (name,surname,password,email) VALUES(%s,%s,%s,%s)"
            self.cur.execute(sql, (name, surname, encrypted_password, email))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False