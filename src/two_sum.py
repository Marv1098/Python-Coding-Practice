def findTwoSum(nums_list, target):
    """
    Check the list if there are two numbers that add up to the target value.
    
    nums: Input of Number List
    target: Input Number value
    """
    # Input Validation:
    if not isinstance(nums_list, list):
        raise TypeError("Input must be a numeric list")
    
    # Empty List Validation
    if len(nums_list) == 0:
        raise ValueError("Cannot find sum from empty list.")
    
    # Non-numeric Validation
    if not all(isinstance(num, (int, float)) for num in nums_list):
        raise TypeError("Input has to be numeric values.")
    
    # Dictionary that maps number to its index in the list
    numsDict = {}
    precision = 10

    # Loop through the list using both index (i) and value (num)
    for i in range(len(nums_list)):
        num = nums_list[i]

        # Compute the number we need to get the target
        num_rounded = round(num, precision)
        diff_rounded = round(target - num, precision)

        # Check if the number we need has already been seen earlier in the list
        if diff_rounded in numsDict:
            print(f"The indices that add up to the value {target} are: {[numsDict[diff_rounded], i]}")
            return [numsDict[diff_rounded], i]
        
        # If not found yet, store the current number and its index
        numsDict[num_rounded] = i
    
    # If the loop ends with no match, there's is no valid pair
    print(f"There are no indices that add up to the target value {target}")
    return None

findTwoSum([1.1, 2.2, 3.3], 3.3)