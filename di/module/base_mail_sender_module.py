from abc import ABC, abstractmethod
from model.mail.base_mail import BaseMail
from model.writer.base_serializable import BaseSerializable


class BaseMailSenderModule(ABC):
    @abstractmethod
    async def send_mail(self, message: BaseMail) -> bool:
        pass

    @abstractmethod
    async def send_serializable(self, message: BaseSerializable) -> bool:
        pass

    @abstractmethod
    def last_mail_sent(self) -> BaseMail:
        pass

