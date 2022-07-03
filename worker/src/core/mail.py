import logging.config
import smtplib
import ssl
from abc import ABC, abstractmethod
from email.message import EmailMessage

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class AbstractEmail(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def send(self, subject: str, address: str, message: str):
        pass

    @abstractmethod
    def close(self):
        pass


class EmailSMTP:
    def __init__(self, host: str, port: int, user: str, password: str, from_email: str = None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.server = None
        self.from_email = from_email

    def connect(self):
        if self.server is None:
            self.server = smtplib.SMTP_SSL(self.host, self.port)
            self.server.login(self.user, self.password)

    def send(self, subject: str, to_email: str, text: str, from_email: str = None):
        if not from_email:
            from_email = self.from_email
        message = EmailMessage()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject
        message.add_alternative(text, subtype='html')
        self.server.sendmail(self.user or from_email, to_email, message.as_string())

    def close(self):
        if self.server is not None:
            self.server.close()


class EmailSMTPFake(EmailSMTP):

    def connect(self):
        logger.info('connect server email')

    def close(self):
        logger.info('disconnect server email')

    def send(self, subject: str, to_email: str, text: str, from_email: str = None):
        if not from_email:
            from_email = self.from_email
        message = EmailMessage()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject
        message.add_alternative(text, subtype='html')
        logger.info(message)


class EmailSmtpSendinblue(EmailSMTP):
    def connect(self):
        if self.server is None:
            context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            self.server = smtplib.SMTP(self.host, self.port)
            self.server.starttls(context=context)
            self.server.login(self.user, self.password)


class EmailSMTPMailhog(EmailSMTP):
    def connect(self):
        if self.server is None:
            # context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            self.server = smtplib.SMTP(self.host, self.port)
            # self.server.starttls(context=context)
            # self.server.login(self.user, self.password)


class EmailSendGrid:
    def __init__(self, api_key: str, from_email: str = None):
        self.api_key = api_key
        self.server = None
        self.from_email = from_email

    def connect(self):
        if self.server is None:
            self.server = SendGridAPIClient(self.api_key)

    def send(self, subject: str, to_email: str, text: str, from_email: str = None):
        if not from_email:
            from_email = self.from_email
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=text)
        self.server.send(message)

    def close(self):
        pass
