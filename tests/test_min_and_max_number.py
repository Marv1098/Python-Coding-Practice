import pytest

from src.min_and_max_number import find_min_and_max

# --------------------
# Valid Input Test
# --------------------
@pytest.mark.parametrize(
    "input_list, expected_min, expected_max",
    [
        ([[5], 5, 5]),                                  # Single Element
        ([1, 2, 3], 1, 3),                              # Normal Case
        ([1, 5, 2, 9, 0], 0, 9),                        # Normal Case
        ([-1, -2, -3], -3, -1),                         # Negative Numbers
        ([4, 4, 4, 4], 4, 4),                           # Identical Numbers
        ([10**100, 5, 10**-100], 10**-100, 10**100)     # Large Numbers
    ]
)
def test_find_min_and_max_values(input_list, expected_min, expected_max):
    min_num, max_num = find_min_and_max(input_list)
    assert min_num == expected_min
    assert max_num == expected_max

# --------------------
# Invalid Input - Raises Error
# --------------------
@pytest.mark.parametrize(
    "invalid_list, expected_error",
    [
        ([], ValueError),               # Empty list
        ([5, 6, "hello"], TypeError),   # Non-numeric values
        (None, TypeError)               # None input
    ]
)
def test_find_min_and_max_invalid(invalid_list, expected_error):
    with pytest.raises(expected_error):
        find_min_and_max(invalid_list)