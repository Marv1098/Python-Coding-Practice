def smallest(nums_list):
    """
    Find the smallest number within the list

    nums_list: Input of list of numbers
    """

    # If the list is empty, raise an exception
    if not nums_list:
        raise ValueError("Cannot find smallest number in a empty list.")

    # Assume the smallest number is the first element
    smallest_so_far = nums_list[0]
    # Loops through each number in the list
    for nums in nums_list:
        # If the current number is smaller that the smallest we've seen,
        # update smallest_so_far to the new smaller number 
        if nums < smallest_so_far:
            smallest_so_far = nums
    
    print("--> Smallest Number in the List: ", smallest_so_far)
    return smallest_so_far