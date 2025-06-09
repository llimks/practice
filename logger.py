from abc import ABC, abstractmethod
from datetime import datetime
import sys

class Formatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass

class SimpleFormatter(Formatter):
    def format(self, message: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {message}"

class Handler(ABC):
    @abstractmethod
    def handle(self, formatted_message: str):
        pass

class StreamHandler(Handler):
    def __init__(self, stream):
        self.stream = stream

    def handle(self, formatted_message: str):
        self.stream.write(formatted_message + "\n")

class Logger:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter
        self.handlers = []

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)

    def log(self, message: str):
        formatted_message = self.formatter.format(message)
        for handler in self.handlers:
            handler.handle(formatted_message)

def main():
    formatter = SimpleFormatter()
    logger = Logger(formatter)

    stderr_handler = StreamHandler(sys.stderr)
    logger.add_handler(stderr_handler)

    logger.log("First log message")
    logger.log("Second log message")

if __name__ == "__main__":
    main()
