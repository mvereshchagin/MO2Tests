def fibonacci(n: int) -> int:
    """
    Computes fibonacci number of n-index
    :param n: index
    :return: fibonacci number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)
