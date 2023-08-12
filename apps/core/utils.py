from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail.backends.smtp import EmailBackend


def send_email(subject: str, emails: list, text_msg: str, html_msg: str, mimetype: str = "text/html"):
    try:
        email = EmailMultiAlternatives(
            # title:
            subject,
            # body text:
            text_msg,
            # from:
            settings.EMAIL_HOST_USER,
            # to:
            emails
        )
        email.attach_alternative(html_msg, mimetype=mimetype)
        email.send()
        return f'Email Sended to {emails}'

    except Exception as e:
        return str(e)


class EmailSender():
    """ Email sender """
    def __init__(self, host=None, port=None, username=None, password=None, use_tls=None, use_ssl=None, timeout=None, ssl_keyfile=None, ssl_certfile=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.use_ssl = use_ssl
        self.timeout = None if timeout == 0 else timeout
        self.ssl_keyfile = ssl_keyfile
        self.ssl_certfile = ssl_certfile

        self.backend = EmailBackend(
            host=self.host,
            port=self.port,
            username=self.username,
            password=password,
            use_tls=self.use_tls,
            use_ssl=self.use_ssl,
            timeout=self.timeout,
            ssl_keyfile=self.ssl_keyfile,
            ssl_certfile=self.ssl_certfile
        )

    def send_email(self, subject: str, emails: list, text_msg: str, html_msg: str, mimetype: str = "text/html"):
        try:
            email = EmailMultiAlternatives(
                # title:
                subject,
                # body text:
                text_msg,
                # from:
                self.host,
                # to:
                emails,
                connection=self.backend
            )
            email.attach_alternative(html_msg, mimetype=mimetype)
            email.send()
            return f'Email Sended to {emails}'

        except Exception as e:
            return str(e)
