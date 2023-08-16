from abc import ABC, abstractmethod

from model.critic_level import CriticLevel
from model.mail.base_mail import BaseMail


class BaseSerializable(ABC):
    @abstractmethod
    def critic_level(self) -> CriticLevel:
        pass

    @abstractmethod
    def serialize(self) -> str:
        pass
