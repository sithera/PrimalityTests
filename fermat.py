from random import randint
from decorators import print_statistics

#@profile
@print_statistics
def is_probable_prime(p, k=7):
    """
    Fermat test that determines whether a number is probable prime
    :param p: number to test
    :param k: test accuracy
    :return: true if number is probable prime, false otherwise
    """
    for _ in range(k):
        a = randint(1, p-1)
        if pow(a, p-1, p) != 1:
            return False
    return True

