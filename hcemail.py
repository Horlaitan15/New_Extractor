import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# import imaplib


class Email:
    def __init__(self):
        self.sender = "sender-email"
        self.receiver = "recipient-email"
        self.password = "google-apppassword"

        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = "Today's Headlines from HackerNew"
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

    def send_email(self, title, link, author, posted, comments):

        content = """"""
        text = """\
            """
        for i in range(len(title)):
            try:
                # Create the body of the message (a plain-text and an HTML version).
                text += f"News for the day\n{title[i].text}\nPosted {posted[i].text} by {author[i].text} | {comments[i].text}\n"
                content += f"""<div style="padding:20px">
                    <h2><a href="{link[i]['href']}"> {title[i].text} </h2></a>
                    <p> Posted {posted[i].text} by {author[i].text} | {comments[i].text}</p> 
                </div><hr/>"""
            except:
                pass

        html = f"""\
        <html>
        <head></head>
        <body>
        <h1> News for the day. </h1><hr\>
        {content}
        </body>
        </html>
        """

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        self.msg.attach(part1)
        self.msg.attach(part2)

        # Create secure connection with server and send email.
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender, self.password)
            server.sendmail(
                self.sender, self.receiver, self.msg.as_string()
            )

        # # Send the message via local SMTP server.
        # s = smtplib.SMTP(host='smtp.gmail.com', port=465)
        # # sendmail function takes 3 arguments: sender's address, recipient's address
        # # and message to send - here it is sent as one string.
        # s.sendmail("ajanihorlaitan@gmail.com", "outlookautomate@gmail.com", self.msg.as_string())
        # print("email sent!")
        # s.quit()


        # self.EMAIL_ACCOUNT = "outlookautomate@gmail.com"
        # self.PASSWORD = "uxzoahsktswpbchh"
        # self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        # self.mail.login(self.EMAIL_ACCOUNT, self.PASSWORD)


