from model.mail.base_mail import BaseMail
from module.base_mail_sender_module import BaseMailSenderModule


class MailSenderModule(BaseMailSenderModule):
    async def send_mail(self, message: BaseMail) -> bool:
        pass

    def last_mail_sent(self) -> BaseMail:
        pass