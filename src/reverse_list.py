def reverse_list(input_list):
    """
    Reverse a given numbers list without using built in reverse()
    """
    # Empty list validation
    if len(input_list) == 0:
        raise ValueError("Cannot reverse a empty list.")
    # Input type validation
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")
    
    reversed_list = []
    for item in range(len(input_list)-1, -1, -1):
        reversed_list.append(input_list[item])

    print("--> List in reverse order: ", reversed_list)
    return reversed_list