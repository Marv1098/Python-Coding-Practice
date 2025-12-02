def num_count(nums_list):
    """
    Counts the occurrences of the numbers in the nums list.
    """
    counts = {}
    for num in nums_list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    print("--> Counts: ", counts)
    return counts

num_count([4,2,4,3,2,4])
