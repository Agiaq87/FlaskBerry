from abc import ABC, abstractmethod
from typing import Optional


class BaseRoute(ABC):
    @abstractmethod
    def connect(self, data: Optional[Optional[str]]) -> str:
        pass

    @abstractmethod
    def delete(self) -> str:
        pass

    @abstractmethod
    def get(self) -> str:
        pass

    @abstractmethod
    def head(self):
        pass

    @abstractmethod
    def options(self) -> str:
        pass

    @abstractmethod
    def patch(self) -> str:
        pass

    @abstractmethod
    def post(self) -> str:
        pass

    @abstractmethod
    def put(self) -> str:
        pass

    @abstractmethod
    def trace(self) -> str:
        pass
