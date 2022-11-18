import unittest
from parameterized import parameterized
from fibonacci import fibonacci


class FibonacciTest(unittest.TestCase):
    def test_fibonacci_pass10_returns55(self):
        # AAA (Arrange, Act, Assert)
        # Arrange

        # Act
        fib10 = fibonacci(10)

        # Assert
        self.assertEqual(fib10, 55)

    def test_fibonacci_pass12_returns100(self):
        # Arrange

        # Act
        fib12 = fibonacci(12)

        # Assert
        self.assertEqual(fib12, 100)

    @parameterized.expand([
        ["fibonacci_test_got_10_returns_55", 10, 55],
        ["fibonacci_test_got_10_returns_65", 10, 65],
        ["fibonacci_test_got_13_returns_233", 13, 233],
        ["fibonacci_test_got_16_returns_987", 16, 987]
    ])
    def test_fibonacci_passVal1_returnsVal2(self, name: str, input_value: int, output_value: int):
        # Arrange

        # Act
        fib_res = fibonacci(input_value)

        # Assert
        self.assertEqual(fib_res, output_value, name)

