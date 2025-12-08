import pytest

from src.two_sum import findTwoSum

# --------------------
# Valid input test
# --------------------
@pytest.mark.parametrize(
    "input_list, target, expected_output",
    [
        ([1, 2, 3, 4], 5, [1, 2]),          # Positive Numbers
        ([-1, -2, -3], -5, [1, 2]),         # Negative Numbers
        ([1.1, 2.2, 3.3], 3.3, [0, 1]),     # Floating point Numbers
        ([1, -1, 2, -3, 4], 6, [2, 4]),     # Mixed Numbers
        ([5], 10, None),                    # Single Element - no valid pair
        ([1, 2, 3], 10, None),              # No valid pair found
        ([0, 0, 0], 0, [0, 1])              # Zeros
    ]
)
def test_find_two_sum_values(input_list, target, expected_output):
    assert findTwoSum(input_list, target) == expected_output

# --------------------
# Invalid input - Raises Error
# --------------------
@pytest.mark.parametrize(
    "bad_input, target, expected_error",
    [
        ([], 10, ValueError),           # Empty String
        ([1, 2, 'a'], 3, TypeError),    # Non-numeric input
        ([None], 10, TypeError),        # None as a number in the list
        ("abc", 5,TypeError)            # Non-list input
    ]
)
def test_find_two_sum_invalid(bad_input, target, expected_error):
    with pytest.raises(expected_error):
        findTwoSum(bad_input, target)