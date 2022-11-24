def use_doctest() -> None:
    import doctest
    doctest.testfile("testfile.txt")


def use_unittest() -> None:
    import unittest

    from fibonacci_unittest import FibonacciTest
    suite = unittest.TestLoader().loadTestsFromTestCase(FibonacciTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    from print_greeting_unittest import PrintGreetingTest
    suite = unittest.TestLoader().loadTestsFromTestCase(PrintGreetingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    from print_greeting_unittest import PrintGreetingTestWithMock
    suite = unittest.TestLoader().loadTestsFromTestCase(PrintGreetingTestWithMock)
    unittest.TextTestRunner(verbosity=2).run(suite)

def try_greeting() -> None:
    from qa import print_greeting2
    from console_io import RealConsoleIO
    console = RealConsoleIO()
    print_greeting2(console)


if __name__ == '__main__':
    # use_doctest()
    use_unittest()
    # try_greeting()

