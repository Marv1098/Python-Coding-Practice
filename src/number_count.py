def num_count(nums_list):
    """
    Counts the occurrences of the numbers in the nums list.
    """
    
    # Checks if the list is empty, if it's raise an exception
    if not nums_list:
        raise ValueError("Couldn't count occurrences in empty list.")
    
    # Validates if the input given is a list, else raise an exception 
    if not isinstance(nums_list, list):
        raise TypeError("nums_list must be a list")
        
    counts = {}
    for num in nums_list:
        # Reject booleans explicitly
        if isinstance(num, bool):
            raise TypeError(f"Boolean value detected: {num!r}")
        # Allow only numeric types
        if not isinstance(num, (int, float)):
            raise TypeError(f"Non-numeric value detected: {num!r}")
        
        # Count the numbers
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    print("--> Counts: ", counts)
    return counts