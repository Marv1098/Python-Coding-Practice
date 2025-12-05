import pytest

from src.remove_duplicates import remove_duplicates

# ------------------------------
# Valid Cases: Unique list output
# ------------------------------
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 1, 2, 3, 4, 4, 4, 5], [1, 2, 3, 4, 5]),                    # Positive Numbers
        ([-1, -1, -2, -2, -3, -4, -5, -5, -5], [-1, -2, -3, -4, -5]),   # Negative Numbers
        (['a', 'a', 'b', 'c', 'b', 'd'], ['a', 'b', 'c', 'd']),         # List of characters
        ([5, 1, 4, 2, 4, 'd', 'a', 'd'], [5, 1, 4, 2, 'd', 'a']),       # Mixed characters and numbers
        ([[1], [1], [2]], [[1], [2]])
    ]
)
def test_remove_duplicate_values(input_list, expected):
    assert remove_duplicates(input_list) == expected

# ------------------------------
# Invalid inputs: non-list
# ------------------------------
@pytest.mark.parametrize(
    "bad_input",
    [
        "abc",  # String
        123,    # Integer
        (1, 2), # Tuple
        None,
    ]
)
def test_remove_duplicates_invalid_type(bad_input):
    with pytest.raises(TypeError):
        remove_duplicates(bad_input)

# ------------------------------
# Booleans are rejected
# ------------------------------
@pytest.mark.parametrize(
    "bool_list",
    [
        [True],
        [False],
        [1, True],
        [False, 0]
    ]
)
def test_remove_duplicates_reject_booleans(bool_list):
    with pytest.raises(TypeError):
        remove_duplicates(bool_list)

# ------------------------------
# Empty List
# ------------------------------
def test_remove_duplicates_empty_list():
    with pytest.raises(ValueError):
        remove_duplicates([])