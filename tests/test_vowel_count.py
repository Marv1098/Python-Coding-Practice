import pytest

from src.vowel_count import count_vowels

# --------------------
# Valid Inputs Test  
# --------------------  
@pytest.mark.parametrize(
    "input_string, expected_count",
    [
        ("Player", 2),  # Normal string
        ("APPLE", 2),    # Upper Case String
        ("rhythm", 0),  # String input with zero vowels
        ("b", 0),  # Single element with zero vowels
        ("a", 1),   # Single with one vowel
        ("aeiouAEIOU", 10)  # Only vowels string
    ]
)
def test_count_vowel(input_string, expected_count):
    assert count_vowels(input_string) == expected_count

# --------------------
# Invalid Input Test - Value Error
# --------------------
@pytest.mark.parametrize(
    "bad_string",
    [
        "", # Empty string
        "hello123", # Non-Alphabetic characters
        "café",     # Accented Vowel
    ]
)
def test_count_vowels_value_error(bad_string):
    with pytest.raises(ValueError):
        count_vowels(bad_string)

# --------------------
# Non-Alphabetic Input - Type Error
# --------------------

@pytest.mark.parametrize(
    "non_string_input",
    [
        123,
        12.34,
        None,
        ["a", "b"],
        {"text": "abc"}
    ]
)
def test_count_vowel_type_error(non_string_input):
    with pytest.raises(TypeError):
        count_vowels(non_string_input)