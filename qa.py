from console_io import ConsoleIO


def print_greeting() -> None:
    print('What is your name?')
    name = input()
    print(f'Hello, {name}')


def print_greeting2(console: ConsoleIO) -> None:
    console.print('What is your name?')
    name = console.input()
    if name == '':
        raise AttributeError('Name can not be empty')
    console.print(f'Hello, {name}')

    console.print('What is your age?')
    age = int(console.input())
    if age <= 18:
        console.print('You are too young for myn app')
    else:
        console.print(f'You are welcome')
