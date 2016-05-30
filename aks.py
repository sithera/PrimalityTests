from decorators import print_statistics


def expand_x_1(n):
    c =1
    for i in range(round(n/2)+1):
        c = c*(n-i)/(i+1)
        yield c


@print_statistics
def is_prime(p):
    if p == 2:
        return True 
    for i in expand_x_1(p):
        if i % p:
            return False
    return True
