import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime
import os 


load_dotenv()
def send_mail(sender,App_Password,receiver,subject,body):
    msg=EmailMessage()
    msg["from"]=sender
    msg["To"]= receiver
    msg["Subject"]=subject



    try:
        msg.set_content(body)
        smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

        #step 5 login using gmail+App Password
        smtp.login(sender,App_Password)

        smtp.send_message(msg)

       
    except Exception as eobj:
        print("This error ",eobj)
    finally:
        smtp.quit()

def main():
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    sender_email="pratiknarule8808@gmail.com"

    #app Password
    app_Password=os.getenv("Sender_Password")

    receiver_mail="pratiknarule88@gmail.com"

    subject=f"This test mail after Time stamp "

    body=f"""Hello Pratik,
    This is  a test email sent from python

    Name:Pratik Narule
    Subject:SMTP Testing
    Status:Sucess
    Testinggggggggggggg

    Thank you

    Regards,
    Python Automation


"""
    send_mail(sender_email,app_Password,receiver_mail,subject,body)

    print("Mail send Sucessfullyy")
   

if __name__=="__main__":
    main()