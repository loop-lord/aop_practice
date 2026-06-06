import pytest
from practice9 import sockMerchant


@pytest.mark.parametrize(
    ("ar", "expected"),
    [
        pytest.param([10, 20, 20, 10, 10, 30, 50, 10, 20], 3, id="sample-input"),
        pytest.param([1, 2, 1, 2, 1, 3, 2], 2, id="problem-statement-example"),
        pytest.param([], 0, id="empty-pile"),
        pytest.param([7], 0, id="single-unmatched-sock"),
        pytest.param([4, 4], 1, id="single-pair"),
        pytest.param([6, 6, 6], 1, id="odd-count-discards-leftover"),
        pytest.param([5, 5, 5, 5], 2, id="two-pairs-same-color"),
        pytest.param([1, 2, 3, 4], 0, id="all-unique-no-pairs"),
        pytest.param([9, 9, 9, 9, 9, 9], 3, id="three-pairs-same-color"),
        pytest.param([1, 1, 2, 2, 3, 3, 3], 3, id="mixed-colors-with-leftover"),
    ],
)
def test_sock_merchant_returns_expected(ar: list[int], expected: int) -> None:
    assert sockMerchant(len(ar), ar) == expected
