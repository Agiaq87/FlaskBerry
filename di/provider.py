from dependency_injector import containers, providers

from di.module.implementation.file_logger_module import FileLoggerModule
from di.module.implementation.logger_publisher_module import LoggerPublisherModule


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()


class LoggerPublisher(containers.DeclarativeContainer):
    logger_publisher = providers.Singleton(LoggerPublisherModule, Container.config)