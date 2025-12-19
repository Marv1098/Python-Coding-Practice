import pytest

from src.palindrome_check import is_palindrome

# --------------------
# Valid Input Test
# --------------------
@pytest.mark.parametrize(
    "valid_input, expected",
    [
        ("RaceCar", True),
        ("A man, a plan, a canal: Panama", True),
        (121, True),
        ("madam", True),
        ("hello", False),
        (123, False),
        ("abc123", False)
    ]
)
def test_is_palindrome_valid(valid_input, expected):
    assert is_palindrome(valid_input) == expected

# --------------------
# Invalid Input Test - Raises Error
# --------------------
@pytest.mark.parametrize(
    "bad_input, expected_error",
    [
        ("", ValueError),
        ("  ", ValueError),
        ("!!!", ValueError),
        ([], TypeError),
        ({}, TypeError),
        (12.34, TypeError)
    ]
)
def test_is_palindrome_raise_error(bad_input, expected_error):
    with pytest.raises(expected_error):
        is_palindrome(bad_input)