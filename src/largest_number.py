def largest(nums_list):
    """
    Returns the largest number within the list
    Raises ValueError if the list is empty
    Raise TypeError it's a Non-list input
    """
    # If the input is a Non-List raise an exception
    if not isinstance(nums_list, (list, tuple)):
        raise TypeError("Input must be a list or tuple of numbers.")

    # If list is empty raise an exception
    if not nums_list:
        raise ValueError("Cannot find the largest number in an empty list.")
    
    # Assume the largest number is -inf
    largest_so_far = float('-inf')
    for i in nums_list:
        if i > largest_so_far:
            largest_so_far = i
    
    print("--> Largest Number in the list: ", largest_so_far)
    return largest_so_far
