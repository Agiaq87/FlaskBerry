from abc import ABC, abstractmethod
from model.mail.base_mail import BaseMail


class BaseMailSenderModule(ABC):
    @abstractmethod
    async def send_mail(self, message: BaseMail) -> bool:
        pass

    @abstractmethod
    def last_mail_sent(self) -> BaseMail:
        pass

