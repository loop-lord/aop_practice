from functools import reduce
from math import gcd


def get_total_x(a: list[int], b: list[int]) -> int:
    """Return how many integers are "between" the arrays ``a`` and ``b``.

    An integer ``x`` is considered "between" ``a`` and ``b`` when:

    1. Every element of ``a`` is a factor of ``x`` (so ``x`` is a common
       multiple of all elements in ``a``).
    2. ``x`` is a factor of every element of ``b`` (so ``x`` divides every
       element in ``b``).

    From (1), any valid ``x`` must be a multiple of ``lcm(a)``. From (2),
    any valid ``x`` must divide ``gcd(b)``. Therefore the answer is the
    number of multiples of ``lcm(a)`` that also divide ``gcd(b)``.
    """
    lcm_a = reduce(lambda x, y: x * y // gcd(x, y), a)
    gcd_b = reduce(gcd, b)

    if gcd_b % lcm_a != 0:
        return 0

    count = 0
    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
    return count


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    assert len(arr) == n
    assert len(brr) == m

    print(get_total_x(arr, brr))
