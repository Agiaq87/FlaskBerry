from di.module.base_mail_sender_module import BaseMailSenderModule
from model.mail.base_mail import BaseMail
from model.writer.base_serializable import BaseSerializable


class MailSenderModule(BaseMailSenderModule):

    def __init__(self, mail_to: str):
        self.__to = mail_to

    async def send_serializable(self, message: BaseSerializable) -> bool:
        pass

    async def send_mail(self, message: BaseMail) -> bool:
        pass

    def last_mail_sent(self) -> BaseMail:
        pass