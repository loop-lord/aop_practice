import pytest
from practice2 import staircase

EXPECTED_N1 = "#\n"

EXPECTED_N4 = """\
   #
  ##
 ###
####
"""

EXPECTED_N6 = """\
     #
    ##
   ###
  ####
 #####
######
"""


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        pytest.param(0, "", id="n=0"),
        pytest.param(1, EXPECTED_N1, id="n=1"),
        pytest.param(4, EXPECTED_N4, id="n=4"),
        pytest.param(6, EXPECTED_N6, id="n=6"),
    ],
)
def test_staircase_matches_expected_output(n: int, expected: str, capsys: pytest.CaptureFixture[str]) -> None:
    staircase(n)
    assert capsys.readouterr().out == expected
