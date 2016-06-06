from fractions import gcd

def fpsp(n, a, b):
    """
    Frobenius test.
    Return True if n is a Frobenius pseudoprime of parameters a, b,
    i.e. with respect to x**2-a*x+b.
    """
    x_0, x_1, x_m, x_mplus1 = _lucas_test_sequence(n, a, b)

    if (x_1 * x_m - x_0 * x_mplus1) % n == 0:
        euler_pow = pow(b, (n-1)//2, n)
        return (euler_pow * x_m) % n == 2
    else:
        return False


def Lucas_chain(n, f, g, x_0, x_1):
    """
    Given an integer n, two functions f and g, and initial value (x_0, x_1),
    compute (x_n, x_{n+1}), where the sequence {x_i} is defined as:
      x_{2i} = f(x_i)
      x_{2i+1} = g(x_i, x_{i+1})
    """
    binary = expand(n, 2)
    u = x_0
    v = x_1
    while binary:
        if 1 == binary.pop():
            u, v = g(u, v), f(v)
        else:
            u, v = f(u), g(u, v)
    return u, v


def _lucas_test_sequence(n, a, b):
    """
    Return x_0, x_1, x_m, x_{m+1} of Lucas sequence of parameter a, b,
    where m = (n - (a**2 - 4*b / n)) // 2.
    """
    d = a**2 - 4*b
    if (d >= 0 and isqrt(d) ** 2 == d) \
    or not(coprime(n, 2*a*b*d)):
        raise ValueError("Choose another parameters.")

    x_0 = 2
    inv_b = inverse(b, n)
    x_1 = ((a ** 2) * inv_b - 2) % n

    # Chain functions
    def even_step(u):
        """
        'double' u.
        """
        return (u**2 - x_0) % n

    def odd_step(u, v):
        """
        'add' u and v.
        """
        return (u*v - x_1) % n

    m = (n - legendre(d, n)) // 2
    x_m, x_mplus1 = Lucas_chain(m, even_step, odd_step, x_0, x_1)

    return x_0, x_1, x_m, x_mplus1


def expand(n, m):
    """
    This function returns m-adic expansion for n.
    n and m should satisfy n > m > 0.
    """
    k = []
    while n // m:
        k.append(n % m)
        n //= m
    k.append(n%m)
    return k

def extgcd(x, y):
    """
    Return a tuple (u, v, d); they are the greatest common divisor d
    of two integers x and y and u, v such that d = x * u + y * v.
    """
    # Crandall & Pomerance "PRIME NUMBERS", Algorithm 2.1.4
    a, b, g, u, v, w = 1, 0, x, 0, 1, y
    while w:
        q, t = divmod(g, w)
        a, b, g, u, v, w = u, v, w, a-q*u, b-q*v, t
    if g >= 0:
        return (a, b, g)
    else:
        return (-a, -b, -g)


def inverse(x, p):
    """
    This function returns inverse of x for modulo p.
    """
    x = x % p
    y = extgcd(p, x)
    if y[2] == 1:
        if y[1] < 0:
            r = p + y[1]
            return r
        else:
            return y[1]
    raise ZeroDivisionError("There is no inverse for %d modulo %d." % (x, p))


def coprime(a, b):
    """
    Return True if a and b are coprime, False otherwise.
    """
    return gcd(a, b) == 1


def legendre(a, m):
    """
    This function returns Legendre symbol (a/m)
    If m is a odd composite then this is Jacobi symbol
    """
    a = a % m
    symbol = 1
    while a != 0:
        while a % 2 == 0:
            a = a//2
            if m % 8 == 3 or m % 8 == 5:
                symbol = -symbol
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            symbol = -symbol
        a = a % m
    if m == 1:
        return symbol
    return 0


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


#print(fpsp(7317713861,23,13))

