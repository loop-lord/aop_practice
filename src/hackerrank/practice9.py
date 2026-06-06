from collections import Counter


def sockMerchant(n: int, ar: list[int]) -> int:
    """Return the number of matching pairs of socks in the pile.

    Socks form a pair when they share the same color. For each color the
    number of complete pairs is the count of that color divided by two,
    discarding any unmatched single sock.

    Args:
        n: The number of socks in the pile. Must equal ``len(ar)``.
        ar: The color of each sock.

    Returns:
        The total number of matching pairs across all colors.
    """
    return sum(count // 2 for count in Counter(ar).values())


if __name__ == "__main__":
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    assert len(ar) == n

    print(sockMerchant(n, ar))
