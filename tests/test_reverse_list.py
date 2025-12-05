import pytest

from src.reverse_list import reverse_list

# --------------------
# Valid cases: Normal lists
# --------------------
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 2, 3], [3, 2, 1]),                         # Positive Numbers
        ([1.5, 2.5, 3.5], [3.5, 2.5, 1.5]),             # Float Values
        ([-1, -2, -3], [-3, -2, -1]),                   # Negative Numbers
        (["a", "b", "c"], ["c", "b", "a"]),             # Characters
        ([[1], [2], [3]], [[3], [2], [1]]),
        ([True, False, True], [True, False, True]),     # Booleans Value
        ([1], [1])  # Single Element
    ]
)
def test_reverse_list_values(input_list, expected):
    assert reverse_list(input_list) == expected

# --------------------
# Invalid Inputs: non-list
# --------------------
@pytest.mark.parametrize(
    "bad_input",
    [
        123,        # Int
        "hello",    # String
        (1, 2, 3),
        None,
        {1: 2},     # Dict
        {1, 2, 3}  # Set
    ]
)
def test_reverse_list_invalid_type(bad_input):
    with pytest.raises(TypeError):
        reverse_list(bad_input)

# --------------------
# Empty List
# --------------------
def test_reverse_list_empty():
    with pytest.raises(ValueError):
        reverse_list([])