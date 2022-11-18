import unittest
import unittest.mock
from console_io import ConsoleIO
from typing import List
from qa import print_greeting2
from parameterized import parameterized

# stub
class MemoryConsoleIO(ConsoleIO):
    _strings = []
    _inputs: List[str]
    _input_pos: int = 0

    def __init__(self, inputs: List[str]):
        self._inputs = inputs
        self._strings = []
        self._input_pos = 0

    def print(self, msg: str) -> None:
        self._strings.append(msg)

    def input(self) -> str:
        if self._input_pos >= len(self._inputs):
            raise IndexError()
        value = self._inputs[self._input_pos]
        self._strings.append(value)
        self._input_pos += 1
        return value

    def print_result(self):
        return '\r\n'.join(self._strings)


class PrintGreetingTest(unittest.TestCase):

    @parameterized.expand([
        ["test_print_greeting_input_Petya", 'Petya', "22"],
        ["test_print_greeting_input_Ivan", 'Ivan', "25"],
        ["test_print_greeting_input_Vasya", 'Vasya', "12"],
        ["test_print_greeting_input_empty", ''],
    ])
    def test_print_greeting_input(self, func_name: str, name: str, age: str):
        # arrange
        console = MemoryConsoleIO([name, age])
        expected_result = f'What is your name?\r\n{name}\r\n' \
                          f'Hello, {name}'\
                          f'\r\nWhat is your age?\r\n' \
                          f'{age}\r\nYou are welcome'

        # act
        print_greeting2(console)
        res = console.print_result()

        # assert
        self.assertEqual(res, expected_result, func_name)


