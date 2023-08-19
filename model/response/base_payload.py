from abc import ABC, abstractmethod


class BasePayload(ABC):

    @abstractmethod
    def jsonify(self) -> str:
        pass

    @abstractmethod
    def require_json_array(self) -> bool:
        pass