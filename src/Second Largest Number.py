def second_largest(nums_list):
    """
    Finds the second largest number in the list
    """
    max_num = nums_list[0]
    second_max_num = nums_list[1]

    for num in nums_list:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num

    print("--> Max Number is: ", max_num)
    print("--> Second Largest Number is: ", second_max_num)
    return second_max_num

second_largest([150, 20, 30, 3, 300, 20, 100])
