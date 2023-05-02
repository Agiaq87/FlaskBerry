from model.writer.base_serializable import BaseSerializable
from module.base_file_writer import BaseFileWriter


class FileLoggerModule(BaseFileWriter):
    async def write_data(self, data: BaseSerializable) -> bool:
        return False

    async def write(self, data: str) -> bool:
        self.file.write(data)

    def __init__(self, file_name: str, protected: bool = False):
        if protected:
            self.filename = f"{file_name}.fblog"
        else:
            self.filename = f"{file_name}.txt"

        self.file = open(self.filename, "a")
