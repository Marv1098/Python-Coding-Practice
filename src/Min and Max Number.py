def find_min_and_max(nums_list):
    """
    The functions finds both Min and Max in the numbers list.
    """

    min_num = nums_list[0]
    max_num = nums_list[0]
    for nums in nums_list:
        if nums < min_num:
            min_num = nums
        if nums > max_num:
            max_num = nums
    
    print(f"--> The Min and Max in the list are: ({min_num,max_num})")
    return min_num, max_num

find_min_and_max([150,20,30,3,5,23,100])
