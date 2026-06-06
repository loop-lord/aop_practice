def diagonalDifference(arr: list[list[int]]) -> int:
    """Return the absolute difference between the sums of the matrix diagonals.

    For a square matrix the primary diagonal runs from the top-left to the
    bottom-right (elements where the row index equals the column index) and the
    secondary diagonal runs from the top-right to the bottom-left (elements
    where the column index mirrors the row index).

    Args:
        arr: A square 2-D array of integers.

    Returns:
        The absolute value of the primary diagonal sum minus the secondary
        diagonal sum.
    """
    n = len(arr)
    primary = sum(arr[i][i] for i in range(n))
    secondary = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)


if __name__ == "__main__":
    n = int(input().strip())

    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

    print(diagonalDifference(arr))
