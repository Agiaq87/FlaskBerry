from abc import ABC, abstractmethod
from model.mail.base_mail import BaseMail


class BaseMailSender(ABC):
    @abstractmethod
    async def send_mail(self, message: BaseMail):
        pass

    @abstractmethod
    def last_mail_sent(self):
        pass

