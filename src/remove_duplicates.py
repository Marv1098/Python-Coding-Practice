def remove_duplicates(input_list):
    """
    Remove Duplicates from the list
    """
    # Validate input type
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")
    
    # Empty list check
    if not input_list:
        raise ValueError("Cannot remove duplicates from empty list.")

    unique_list=[]
    for item in input_list:
        # Checks for boolean in the list, if boolean detected raise exception
        if isinstance(item, bool):
            raise TypeError(f"Boolean value detected: {item!r}")
        
        if item not in unique_list:
            unique_list.append(item)
        
    print("--> Updated List: ", unique_list)
    return unique_list