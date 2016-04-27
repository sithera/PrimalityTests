from random import randint


def is_probable_prime(p, k):
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

#  Tests
for i in range(0, 10):
    p = randint(0, 5000000000000)
    print("Number: " + str(p) + " is prime: " + str(is_probable_prime(p, 10000)))
