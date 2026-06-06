import pytest
from practice11 import pageCount


@pytest.mark.parametrize(
    ("n", "p", "expected"),
    [
        pytest.param(6, 2, 1, id="sample-input-0"),
        pytest.param(5, 4, 0, id="sample-input-1"),
        pytest.param(5, 3, 1, id="problem-statement-example"),
        pytest.param(6, 5, 1, id="from-back-odd-page"),
        pytest.param(6, 6, 0, id="last-page-even-book"),
        pytest.param(7, 4, 1, id="even-page-odd-book"),
        pytest.param(1, 1, 0, id="single-page-book"),
        pytest.param(4, 1, 0, id="first-page"),
        pytest.param(100000, 1, 0, id="first-page-large-book"),
        pytest.param(100000, 100000, 0, id="last-page-large-book"),
        pytest.param(100000, 50000, 25000, id="middle-page-large-book"),
    ],
)
def test_page_count_returns_expected(n: int, p: int, expected: int) -> None:
    assert pageCount(n, p) == expected


@pytest.mark.parametrize("n", [1, 2, 7, 8, 99, 100])
def test_page_count_is_minimum_of_both_directions(n: int) -> None:
    for p in range(1, n + 1):
        expected = min(p // 2, n // 2 - p // 2)
        assert pageCount(n, p) == expected
