import pytest
from practice6 import get_total_x


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        pytest.param([2, 4], [16, 32, 96], 3, id="sample-0-three-between"),
        pytest.param([2, 6], [24, 36], 2, id="problem-statement-example"),
        pytest.param([1], [100], 9, id="all-divisors-of-100"),
        pytest.param([3, 4], [24, 48], 2, id="lcm-12-divides-gcd-24"),
        pytest.param([7], [2, 3, 5], 0, id="no-common-integer"),
        pytest.param([5, 10], [15, 30], 0, id="lcm-does-not-divide-gcd"),
        pytest.param([1], [1], 1, id="single-trivial-one"),
        pytest.param([100], [100], 1, id="single-equal-max"),
        pytest.param([2, 3, 4, 5], [60, 120], 1, id="lcm-equals-gcd"),
        pytest.param([1, 2], [50, 100], 3, id="even-divisors-of-50"),
    ],
)
def test_get_total_x_returns_expected(a: list[int], b: list[int], expected: int) -> None:
    assert get_total_x(a, b) == expected
