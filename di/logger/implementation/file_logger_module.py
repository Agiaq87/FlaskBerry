from di.logger.base_file_writer_module import BaseFileWriterModule
from model.writer.base_serializable import BaseSerializable


class FileLoggerModule(BaseFileWriterModule):
    async def write_data(self, data: BaseSerializable) -> bool:
        return False

    async def write(self, data: str) -> bool:
        return self.file.write(data) != 0

    def __init__(self, file_name: str, protected: bool = False):
        if protected:
            self.filename = f"{file_name}.log"
        else:
            self.filename = f"{file_name}.txt"

        self.file = open(self.filename, "a")
