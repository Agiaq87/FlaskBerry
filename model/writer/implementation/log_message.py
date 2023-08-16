from model.critic_level import CriticLevel
from model.writer.base_serializable import BaseSerializable


class LogMessage(BaseSerializable):

    def __init__(self, json: str, critical_level: CriticLevel = CriticLevel.INFO):
        self.__critic_level = critical_level
        self.__json = json

    def critic_level(self) -> CriticLevel:
        return self.__critic_level

    def serialize(self) -> str:
        return self.__json
