from abc import ABC, abstractmethod
from typing import List

from model.critic_level import CriticLevel
from model.mail.mail_object import MailObject
from model.mail.mail_subject import MailSubject


class BaseMail(ABC):
    @abstractmethod
    def to(self) -> MailSubject:
        pass

    @abstractmethod
    def cc(self) -> List[MailSubject]:
        pass

    @abstractmethod
    def object(self) -> MailObject:
        pass

    @abstractmethod
    def critic_level(self) -> CriticLevel:
        pass
