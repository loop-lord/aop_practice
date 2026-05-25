def countApplesAndOranges(
    s: int,
    t: int,
    a: int,
    b: int,
    apples: list[int],
    oranges: list[int],
) -> None:
    """Print how many apples and oranges land on Sam's house.

    The house spans the inclusive range ``[s, t]`` on the x-axis. The apple
    tree is located at ``a`` and the orange tree at ``b``. Each entry in
    ``apples``/``oranges`` is a signed distance ``d`` from its tree of origin,
    so a fruit's landing position is ``tree + d``.
    """
    apple_count = sum(1 for d in apples if s <= a + d <= t)
    orange_count = sum(1 for d in oranges if s <= b + d <= t)

    print(apple_count)
    print(orange_count)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    _m = int(third_multiple_input[0])
    _n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
