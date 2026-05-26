import pytest
from practice8 import migratory_birds


@pytest.mark.parametrize(
    ("arr", "expected"),
    [
        pytest.param([1, 4, 4, 4, 5, 3], 4, id="sample-0-clear-winner"),
        pytest.param([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4], 3, id="sample-1-tie-pick-smallest"),
        pytest.param([1, 1, 2, 2, 3], 1, id="problem-statement-example"),
        pytest.param([5], 5, id="single-sighting"),
        pytest.param([3, 3, 3, 3], 3, id="all-same-type"),
        pytest.param([1, 2, 3, 4, 5], 1, id="all-unique-pick-smallest-id"),
        pytest.param([5, 5, 4, 4, 3, 3, 2, 2, 1, 1], 1, id="full-tie-across-all-types"),
        pytest.param([2, 2, 2, 5, 5, 5, 1], 2, id="tie-between-non-min-ids"),
        pytest.param([4, 4, 4, 4, 1], 4, id="dominant-non-min-id"),
    ],
)
def test_migratory_birds_returns_expected(arr: list[int], expected: int) -> None:
    assert migratory_birds(arr) == expected
