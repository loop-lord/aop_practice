import pytest
from practice4 import countApplesAndOranges


@pytest.mark.parametrize(
    ("s", "t", "a", "b", "apples", "oranges", "expected_apples", "expected_oranges"),
    [
        pytest.param(7, 11, 5, 15, [-2, 2, 1], [5, -6], 1, 1, id="sample-0"),
        pytest.param(7, 10, 4, 12, [2, 3, -4], [3, -2, -4], 1, 2, id="problem-example"),
        pytest.param(2, 3, 1, 5, [], [], 0, 0, id="no-fruits"),
        pytest.param(1, 100, 50, 60, [0, -49, 50], [-59, 40, 0], 3, 3, id="all-inside"),
        pytest.param(10, 20, 5, 25, [1, 2, 3], [1, 2, 3], 0, 0, id="all-outside"),
        pytest.param(5, 5, 3, 7, [2, 3, -1], [-2, 0, 1], 1, 1, id="single-point-house"),
        pytest.param(7, 11, 5, 15, [2], [-4], 1, 1, id="boundary-equals-s"),
        pytest.param(7, 11, 5, 15, [6], [-4], 1, 1, id="boundary-equals-t"),
        pytest.param(7, 11, 5, 15, [1, 7], [-9, -3], 0, 0, id="just-outside-boundaries"),
    ],
)
def test_count_apples_and_oranges_prints_expected(
    s: int,
    t: int,
    a: int,
    b: int,
    apples: list[int],
    oranges: list[int],
    expected_apples: int,
    expected_oranges: int,
    capsys: pytest.CaptureFixture[str],
) -> None:
    countApplesAndOranges(s, t, a, b, apples, oranges)
    captured = capsys.readouterr()
    assert captured.out == f"{expected_apples}\n{expected_oranges}\n"
