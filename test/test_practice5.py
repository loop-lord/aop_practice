import pytest
from practice5 import kangaroo


@pytest.mark.parametrize(
    ("x1", "v1", "x2", "v2", "expected"),
    [
        pytest.param(0, 3, 4, 2, "YES", id="sample-0-meet-after-4-jumps"),
        pytest.param(0, 2, 5, 3, "NO", id="sample-1-second-faster"),
        pytest.param(0, 3, 2, 1, "YES", id="meet-after-two-jumps"),
        pytest.param(0, 2, 5, 2, "NO", id="equal-speeds-different-start"),
        pytest.param(0, 5, 10, 5, "NO", id="equal-speeds-never-meet"),
        pytest.param(0, 4, 3, 2, "NO", id="gap-not-divisible-by-speed-diff"),
        pytest.param(0, 3, 6, 1, "YES", id="meets-after-three-jumps"),
        pytest.param(0, 10000, 10000, 1, "NO", id="boundary-large-not-divisible"),
        pytest.param(0, 10000, 9999, 1, "YES", id="boundary-large-divisible"),
        pytest.param(43, 2, 70, 2, "NO", id="equal-speeds-positive-gap"),
    ],
)
def test_kangaroo_returns_expected(x1: int, v1: int, x2: int, v2: int, expected: str) -> None:
    assert kangaroo(x1, v1, x2, v2) == expected
