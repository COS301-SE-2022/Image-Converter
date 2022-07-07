import os
import sys
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

load_dotenv()

class Email:

    sg = None

    def __init__(self):
        try:
            self.sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

        except Exception as e:
            print("THE ERROR IS", e)

    def sendMessage(self, reciver_email, message):
        message = Mail(
                       from_email="hardcode810@gmail.com",
                       to_emails=reciver_email,
                       subject="Verification Code",
                       plain_text_content=message,
                       html_content="<p>"+message+"</p>")
        try:
            response = self.sg.send(message)
            print(response.status_code)
        except Exception as e:
            print("Exception error", e)
