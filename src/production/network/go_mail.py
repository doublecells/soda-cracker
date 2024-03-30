"""
Class - Mail send process class
"""
import os
import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.utils import make_msgid, formataddr
from email.header import Header

class GoMail:
    """
    A class sending email to receiver individually
    """

    def __init__(self, entity) -> None:
        self._entity = entity

    def send(self):
        """
        Sends email to receiver with context.
        """
        email = EmailMessage()
        email['Subject'] = self._entity.subject
        email['From'] = formataddr((str(Header(self._entity.from_addr[0], 'utf-8')), self._entity.from_addr[1]))
        asparaus_cid = make_msgid()
        email.add_alternative(
            self._entity.message.format(
                asparaus_cid = asparaus_cid[1:-1]),
            subtype = 'html')

        # -- Add attachment
        if self._entity.attachments is not None:
            for _attach in self._entity.attachments:
                self._add_attachment(email, _attach)

        sender = smtplib.SMTP(self._entity.host)
        for addr in self._entity.to_addrs:
            del email['To']
            email['To'] = addr
            sender.send_message(email)
        sender.quit()
    
    def _add_attachment(self, _mail, _file):
        with open(_file, mode="rb") as f:
            _file_data = f.read()
            _maintype, _, _subtype = (mimetypes.guess_type(_file)[0] \
                                      or 'application/octet-stream').partition("/")
            _mail.add_attachment(_file_data,
                                 maintype=_maintype,
                                 subtype=_subtype, 
                                 filename=self._capture_file_name_only(_file))

    def _capture_file_name_only(self, path):
        return os.path.basename(path)