import pytest

from src.smallest_number import smallest

@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([5,2,9,1,7], 1),       # Positive Numbers
        ([-3,-7,-1,-9], -9),    # Negative Numbers
        ([3,-2,7,0,-5], -5),    # Mixed Numbers
        ([2,2,3,1,1], 1),       # Duplicates
        ([42], 42)              # Single Element
    ]
)
def test_smallest_values(input_list, expected):
    assert smallest(input_list) == expected

def test_empty_list_raises_exception():
    with pytest.raises(ValueError):
        smallest([])