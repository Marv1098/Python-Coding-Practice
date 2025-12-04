def second_largest(nums_list):
    """
    Finds the second largest number in the list
    """

    if len(nums_list) < 2:
        raise ValueError("List must have at least two distinct numbers.")
    
    max_num = second_max_num = float('-inf')
    
    for num in nums_list:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num != max_num and num > second_max_num:
            second_max_num = num

    if second_max_num == float('-inf'):
        raise ValueError("No second largest value exists (all elements are equal).")

    print("--> Max Number is: ", max_num)
    print("--> Second Largest Number is: ", second_max_num)
    return second_max_num

#second_largest([150, 20, 30, 3, 300, 20, 100])
#second_largest([35,35,35])
