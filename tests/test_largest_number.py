import pytest

from largest_number import largest

@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 2, 3, 4, 5], 5),               # Postive Numbers
        ([-3, -1, -7, -10, -5], -1),        # Negative Numbers
        ([3, -2, 7, 0, -5], 7),             # Mixed Numbers
        ([1e308, 1e309], float('inf')),     # Large Floats
        ([5, 5, 5, 5, 5], 5),               # All Elements Same
        ([42], 42)                          # Single Element
    ]
)
def test_largest_values(input_list, expected):
    largest(input_list)

def test_empty_list_raises_exception():
    with pytest.raises(ValueError):
        largest([])

def test_non_list_raises_exception():
    with pytest.raises(TypeError):
        largest('abc')