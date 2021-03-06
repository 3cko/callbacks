import smtplib


class SendMail():
    def __init__(self, recipient, ddi, ticket, name, phone, platform, details, status,id):
        self.recipient = recipient
        self.platform = platform
        self.details = details
        self.status = status
        self.id = id
        self.ticket = ticket
        self.phone = phone
        self.name = name
        self.ddi = ddi

    def run(self):
        message = """From: CallBack <postmaster@cb.ohaiworld.com>
To: {0}
Subject: {7}: {6} Call Back - Ticket {4}
In-Reply-To: {8}
Message-ID: {8}
References: {8}
Thread-Topic: {6} Call Back - Ticket {4}
Thread-Index: {8}

DDI: {1}
Name: {2}
Phone Number: {3}
Ticket: https://some.url.com/tickets/{4}
Callback: http://192.237.219.96:8182/callbacks/{8}

Call Details:
{5}
        """.format(self.recipient,
                   self.ddi,
                   self.name,
                   self.phone,
                   self.ticket,
                   self.details,
                   self.platform,
                   self.status,
                   self.id
                   )
        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail('test@domain.com', self.recipient, message)
            return message
        except SMTPException,e:
            print e
            return "Error: Unable to send email"
