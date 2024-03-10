from src.application.adapter.emailService import AdapterServerEmail

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

from src.notificate.view.__path__ import DIR

import pathlib

import os

from src.infra.repository import Repository



class Email:
    def __init__(self):
        self.__host = os.getenv("EMAIL_HOST_SERVER")
        self.__port = os.getenv("EMAIL_PORT_SERVER")
        self.__pwd = os.getenv("EMAIL_PASSWORD")
        self.__user = os.getenv("EMAIL_USER")

        self.__connect()

    def __connect(self):
        """connect to de server email and login"""
        try:
            self.server = AdapterServerEmail(
                host_=self.__host,
                port_=self.__port
            ).server()

            self.server.ehlo()
            self.server.starttls()
            self.server.\
                login(
                    user=self.__user,
                    password=self.__pwd
                )
        except Exception as error:
            print(error)
            print("Error conecting, check your internet connection!")
        else:
            self.MIMEMessage = MIMEMultipart()

    def send(self):
        """send email for susbcribers"""
        self.format_message()

        self.MIMEMessage["From"] = self.__user
        self.MIMEMessage["Subject"] = "Notícias actualizadas do país"

        self.MIMEMessage.attach(MIMEText(self.messageModel, "html"))

        self.server.sendmail(
            self.MIMEMessage["From"], 
            Email.get_emails(), 
            self.MIMEMessage.as_string().encode("utf-8")
        )
        self.server.quit()
    

    def format_message(self):
        """construct the model of the message"""
        html = f"{pathlib.Path(f'{DIR}/message.html').read_text()}"
        newspappers = Repository.get_all_newspapper()
        self.messageModel = "<body>"

        for item in newspappers:
            __message = html.replace("{m_category}", item["category"]).\
                replace("{m_header}", str(item["header"])).\
                    replace("{m_datePublish}", str(item["date_publish"])).\
                        replace("{m_content}", str(item["content"]))
            self.messageModel += f"\n{__message}"
        self.messageModel += "\n</body>"


    @staticmethod
    def get_emails():
        """get all emails subscribers"""
        entitys = Repository.get_all_email()
        __emails = list()

        for item in entitys:
            __emails.append(
                item["email"]
            )
        return __emails