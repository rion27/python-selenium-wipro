import pytest

@pytest.mark.parametrize(
    "input_value, expected",
    [
        (1, 2),
        (2, 4),
        pytest.param(3, 6, marks=pytest.mark.xfail(reason="Known bug #101")),
        pytest.param(4, 8, marks=pytest.mark.xfail(reason="Known bug #102")),
        (5, 10),
    ]
)
def test_double_function(input_value, expected):
    assert input_value * 2 == expected
