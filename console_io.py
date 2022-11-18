from abc import ABC


class ConsoleIO(ABC):
    def print(self, msg: str) -> None:
        pass

    def input(self) -> str:
        pass


class RealConsoleIO(ConsoleIO):
    def print(self, msg: str) -> None:
        print(msg)

    def input(self) -> str:
        return input()
