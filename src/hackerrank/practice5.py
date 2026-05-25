def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    """Return ``"YES"`` if both kangaroos can land on the same position.

    Kangaroo 1 starts at ``x1`` jumping ``v1`` meters per jump, kangaroo 2
    starts at ``x2`` jumping ``v2`` meters per jump. After ``n`` jumps their
    positions are equal iff::

        x1 + n * v1 == x2 + n * v2
        => n = (x2 - x1) / (v1 - v2)

    Since the constraints guarantee ``x1 < x2``, kangaroo 1 can only catch
    kangaroo 2 when ``v1 > v2`` and the gap divides evenly by the speed
    difference (so ``n`` is a non-negative integer).
    """
    if v1 <= v2:
        return "NO"
    return "YES" if (x2 - x1) % (v1 - v2) == 0 else "NO"


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])

    print(kangaroo(x1, v1, x2, v2))
