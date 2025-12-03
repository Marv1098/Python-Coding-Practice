def largest(nums_list):
    """
    Returns the largest number within the list
    """

    largest_so_far = nums_list[0]
    for i in nums_list:
        if i > largest_so_far:
            largest_so_far = i
    
    print("--> Largest Number in the list: ", largest_so_far)
    return largest_so_far

largest([150,20,30,3,5,23,100])
