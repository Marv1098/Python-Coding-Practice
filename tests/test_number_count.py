import pytest

from src.number_count import num_count

@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 1, 2, 2, 3, 4, 5, 5, 5], {1: 2, 2: 2, 3: 1, 4: 1, 5: 3}),                  # Positive Numbers
        ([-1, -1, -2, -2, -3, -4, -5, -5, -5], {-1: 2, -2: 2, -3: 1, -4: 1, -5: 3}),    # Negative Numbers
        ([-1, -1, 2, 2, -3, -4, -4, 5, 5], {-1: 2, 2: 2, -3: 1, -4: 2, 5: 2}),          # Mixed Numbers
        ([42], {42: 1}),                                                                # Single Element
        ([1, 2], {1: 1, 2: 1}),                                                         # Two Elements
        ([1.5, 1.5, 3], {1.5: 2, 3: 1})                                                 # Float Numbers
    ]
)

def test_num_count_values(input_list, expected):
    assert num_count(input_list) == expected

@pytest.mark.parametrize(
    "bad_input",
    [
        "123",          # String
        100,            # Integer, not list
        (1, 2),         # Tuple
        ["a", 1],       # Non-numeric list
        [None],
        [[1], [2]],     # Unhashasble elements
        [{"x": 1}],
        [True, False]   # Booleans rejected
    ]
)

def test_num_count_invalid_input_raise_exception(bad_input):
    with pytest.raises(TypeError):
        num_count(bad_input)

def test_empty_list_raise_exception():
    with pytest.raises(ValueError):
        num_count([])