import pytest
from practice10 import diagonalDifference


@pytest.mark.parametrize(
    ("arr", "expected"),
    [
        pytest.param([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15, id="sample-input"),
        pytest.param([[1, 2, 3], [4, 5, 6], [9, 8, 9]], 2, id="problem-statement-example"),
        pytest.param([[5]], 0, id="single-element"),
        pytest.param([[1, 2], [3, 4]], 0, id="two-by-two-equal-diagonals"),
        pytest.param([[1, 0], [0, 0]], 1, id="two-by-two-nonzero-difference"),
        pytest.param([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 2, id="identity-matrix"),
        pytest.param([[-100, 0, 0], [0, 0, 0], [0, 0, -100]], 200, id="negative-bounds"),
        pytest.param([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, id="all-zeros"),
        pytest.param(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            0,
            id="four-by-four-equal-diagonals",
        ),
    ],
)
def test_diagonal_difference_returns_expected(arr: list[list[int]], expected: int) -> None:
    assert diagonalDifference(arr) == expected
