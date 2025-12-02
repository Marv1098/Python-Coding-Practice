def smallest(nums_list):
    """
    Find the smallest number within the list
    """
    smallest_so_far = nums_list[0]
    for nums in nums_list:
        if nums < smallest_so_far:
            smallest_so_far = nums
    
    print("--> Smallest Number in the List: ", smallest_so_far)
    return smallest_so_far

smallest([150,20,30,3,5,23,100])