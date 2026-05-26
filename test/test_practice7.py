import pytest
from practice7 import breaking_records


@pytest.mark.parametrize(
    ("scores", "expected"),
    [
        pytest.param(
            [10, 5, 20, 20, 4, 5, 2, 25, 1],
            [2, 4],
            id="sample-0-mixed-records",
        ),
        pytest.param(
            [3, 4, 21, 36, 10, 28, 35, 5, 24, 42],
            [4, 0],
            id="sample-1-only-max-broken",
        ),
        pytest.param([10], [0, 0], id="single-game-no-breaks"),
        pytest.param([7, 7, 7, 7], [0, 0], id="all-ties-never-break"),
        pytest.param([1, 2, 3, 4, 5], [4, 0], id="strictly-increasing"),
        pytest.param([5, 4, 3, 2, 1], [0, 4], id="strictly-decreasing"),
        pytest.param([0, 0, 0], [0, 0], id="all-zeros"),
        pytest.param([10, 10, 11, 9, 9, 12, 8], [2, 2], id="ties-then-breaks"),
        pytest.param([50, 100, 0, 100, 0, 50], [1, 1], id="repeat-extremes-not-counted"),
    ],
)
def test_breaking_records_returns_expected(scores: list[int], expected: list[int]) -> None:
    assert breaking_records(scores) == expected
