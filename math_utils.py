# Create a module that contains certain functions

def factorial(n: int) -> int:
    """
    Return factorial of given number.
    Arguments:
        n: Given number whose factorial is to be found
    Returns:
        int: Returns the factorial of n
    Exceptions:
        TypeError: If n is not an int
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative number")

    return 1 if (n == 0) else (n * factorial(n- 1))

def gcd(a: int, b: int) -> int:
    """
    Calculates GCD of given numbers
    Arguments:
        a, b: integers whose GCD is to be found
    Returns:
        int: GCD of a, b
    Exceptions:
        TypeError: If a, b is not an integer
    """

    while a != b:
        if a > b:
            a, b = a - b, b
        else:
            a, b = a, b - a

    return a

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime
    Arguments:
        n: The number to be checked
    Returns:
        bool: True if prime, else false
    Exceptions:
        TypeError: if n is not an int
        ValueError: if n is non-positive or if n < 2
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")

    if n < 2:
        raise ValueError("This number is neither prime nor composite")
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n):
            if n % i == 0:
                return False
    return True