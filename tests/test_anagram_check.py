import pytest

from src.anagram_check import clean_text, is_anagram

# --------------------
# Valid Input Test - clean_text()
# --------------------
@pytest.mark.parametrize(
        "input_str, expected",
        [
            ("abc", ["a", "b", "c"]),
            ("A B C", ["a", "b", "c"]),
            ("A!b@C#", ["a", "b", "c"]),
            ("123", ["1", "2", "3"]),
            ("A\tB\nC", ["a", "b", "c"]),
            ("", []),
            ("!!!", [])
        ]
)
def test_clean_text(input_str, expected):
    assert clean_text(input_str) == expected

# --------------------
# Valid Input Test - is_anagram()
# --------------------

@pytest.mark.parametrize(
    "input_str1, input_str2, expected",
    [
        ("listen", "silent", True),
        ("the eyes", "they see", True),
        ("rail safety!", "fairy tales", True),
        ("hello", "world", False),
        ("abc", "ab", False),
        ("aabbcc", "abcabc", True),
        ("test", "tsett", False)
    ]
)
def test_is_anagram_valid_cases(input_str1, input_str2, expected):
    assert is_anagram(input_str1, input_str2) == expected

# --------------------
# Invalid Input - Raises Error
# --------------------
@pytest.mark.parametrize(
    "bad_input1, bad_input2, error",
    [
        (123, "abc", TypeError),
        ("abc", None, TypeError),
        ([], "abc", TypeError),
        ("abc", {}, TypeError),
        ("", "listen", ValueError),
        (" ", "", ValueError),
        ("!!!", "???", ValueError)
    ]
)
def test_is_anagram_raise_error(bad_input1, bad_input2, error):
    with pytest.raises(error):
        is_anagram(bad_input1, bad_input2)