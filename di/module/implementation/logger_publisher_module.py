from config.flask_berry_config import FlaskBerryConfig
from di.module.base_file_writer_module import BaseFileWriterModule
from di.module.base_logger_publisher_module import BaseLoggerPublisherModule
from di.module.base_mail_sender_module import BaseMailSenderModule
from model.critic_level import CriticLevel
from model.writer.implementation.log_message import LogMessage


class LoggerPublisherModule(BaseLoggerPublisherModule):
    def __init__(self, file_writer: BaseFileWriterModule, mail_sender: BaseMailSenderModule, config: FlaskBerryConfig):
        self.__file = file_writer
        self.__mail = mail_sender
        self.__config = config

    def log(self, log_message: LogMessage):
        if log_message.critic_level() != CriticLevel.INFO:
            self.__mail.send_mail()

