def remove_duplicates(nums_list):
    """
    Remove Duplicates from the list
    """
    unique_list=[]
    for num in nums_list:
        if num not in unique_list:
            unique_list.append(num)
        
    print("--> No Duplicates List: ",unique_list)
    return unique_list

remove_duplicates([150,20,30,3,5,5,150,20,100])