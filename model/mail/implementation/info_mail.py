from typing import List

from model.critic_level import CriticLevel
from model.mail.base_mail import BaseMail
from model.mail.mail_object import MailObject
from model.mail.mail_subject import MailSubject


class InfoMail(BaseMail):

    def to(self) -> MailSubject:
        return self.__to_mail

    def cc(self) -> List[MailSubject]:
        return self.__cc

    def object(self) -> MailObject:
        return self.__object_mail

    def critic_level(self) -> CriticLevel:
        return self.__critic_level

    def __init__(self, to_mail: str, object_mail: str, cc: List[str]):
        self.__to_mail = MailSubject(to_mail)
        self.__object_mail = MailObject(object_mail)
        self.__cc = [MailSubject(x) for x in cc]
        self.__critic_level = CriticLevel.INFO

