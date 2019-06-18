import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

class MyMail():
    def __init__(self, server, port, email, password):
        self.server = server
        self.port = port
        self.email = email
        self.password = password

    def __del__(self):
        self.s.quit()

    def toMail(self, mail):
        self.mailList = mail
    
    def message_generate(self, subject, body):
        self.msg = MIMEMultipart()
        self.msg['From'] = self.email
        self.msg['To'] = self.mailList
        self.msg['Subject'] = subject
        self.body = body
        self.msg.attach(MIMEText(self.body, 'plain'))

    def attachment_file(self, filename, path = "\\"):
        self.filename = filename
        self.path = path
        self.p = MIMEBase('application', 'octet-stream')
        self.attachment = open(self.path + self.filename, "rb")
        self.p.set_payload((self.attachment).read())
        encoders.encode_base64(self.p)
        self.p.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
        self.msg.attach(self.p)

    def send_mail(self):
        self.s = smtplib.SMTP(self.server, self.port)
        self.s.starttls()
        self.s.login(self.email, self.password)
        self.text = self.msg.as_string()
        self.s.sendmail(self.email, self.mailList, self.text)