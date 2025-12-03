def reverse_list(nums_list):
    """
    Reverse a given numbers list without using built in reverse()
    """
    reversed_list = []
    for num in nums_list[::-1]:
        reversed_list.append(num)

    print("--> List in reverse order: ",reversed_list)
    return reversed_list

reverse_list([2,3,20,30,45,100,150])
