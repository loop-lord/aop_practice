import pytest
from practice3 import gradingStudents


@pytest.mark.parametrize(
    ("grades", "expected"),
    [
        pytest.param([73, 67, 38, 33], [75, 67, 40, 33], id="sample-0"),
        pytest.param([84], [85], id="round-up-84-to-85"),
        pytest.param([29], [29], id="below-38-not-rounded"),
        pytest.param([57], [57], id="diff-three-not-rounded"),
        pytest.param([38], [40], id="boundary-38-rounds-up"),
        pytest.param([37], [37], id="boundary-37-not-rounded"),
        pytest.param([100], [100], id="max-grade-unchanged"),
        pytest.param([0], [0], id="min-grade-unchanged"),
        pytest.param([], [], id="empty-list"),
        pytest.param([40, 45, 50], [40, 45, 50], id="exact-multiples-unchanged"),
    ],
)
def test_grading_students_matches_expected(grades: list[int], expected: list[int]) -> None:
    assert gradingStudents(grades) == expected
