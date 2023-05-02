from abc import ABC, abstractmethod

from model.writer.base_serializable import BaseSerializable


class BaseFileWriter(ABC):
    @abstractmethod
    async def write(self, data: str) -> bool:
        pass

    @abstractmethod
    async def write_data(self, data: BaseSerializable) -> bool:
        pass
