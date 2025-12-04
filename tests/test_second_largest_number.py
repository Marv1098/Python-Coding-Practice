import pytest

from src.second_largest_number import second_largest

@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([150, 10, 30, 20, 15], 30),        # Positive Numbers
        ([-100, -10, -35, -50, -5], -10),   # Negative Numbers
        ([150, -100, 35, 90, -15], 90),     # Mixed Numbers
        ([3, 7], 3)                         # Two Elements
    ]
)
def test_second_largest_values(input_list, expected):
    assert second_largest(input_list) == expected

def test_empty_list_raises_exception():
    with pytest.raises(ValueError):
        second_largest([])

def test_single_element_raises_exception():
    with pytest.raises(ValueError):
        second_largest([42])

def test_two_element_duplicates_raises_exception():
    with pytest.raises(ValueError):
        second_largest([42, 42])

def test_all_same_elements_raises_exception():
    with pytest.raises(ValueError):
        second_largest([42, 42, 42])
