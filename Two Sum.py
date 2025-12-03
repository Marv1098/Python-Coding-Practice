def findTwoSum(nums, target):
    """
    Check the list if there are two numbers that add up to the target value.
    
    nums: Input of Number List
    target: Input Number value
    """

    # Dictionary that maps number to its index in the list
    numsDict = {}

    # Loop through the list using both index (i) and value (num)
    for i, num in enumerate(nums):

        # Compute the number we need to get the target
        diff = target - num

        # Check if the number we need has already been seen earlier in the list
        if diff in numsDict:
            print(f"The indices that add up to the value {target} are: {[numsDict[diff], i]}")
            return [numsDict[diff], i]
        
        # If not found yet, store the current number and its index
        numsDict[num] = i
    
    # If the loop ends with no match, there's is no valid pair
    print(f"There are no indices that add up to the target value {target}")
    return None

findTwoSum([1,3,7,9,2], 11)
