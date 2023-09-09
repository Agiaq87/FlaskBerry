from abc import ABC, abstractmethod

from model.writer.implementation.log_message import LogMessage


class BaseLoggerPublisherModule(ABC):
    @abstractmethod
    def log(self, log_message: LogMessage):
        pass