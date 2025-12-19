def clean_text(text):
    result = []
    for c in text:
        if c.isalnum():
            result.append(c.lower())
    return result

def is_anagram(text1, text2):
    """
    This function checks if the following two text1 & text2 are anagrams.
    
    text1: String input
    text2: String input
    """
    
    # Type Validation
    if not isinstance(text1, str):
        raise TypeError("The input must be a string.")
    if not isinstance(text2, str):
        raise TypeError("The input must be a string.")

    text1_clean = clean_text(text1)
    text2_clean = clean_text(text2)

    # Empty String Validation
    if not text1_clean or not text2_clean:
        raise ValueError("Inputs must contain at least one non-space character.")

    if len(text1_clean) != len(text2_clean):
        print(f"Length of {text1} & {text2} are not equal therefore they are not Anagram.")
        return False

    freq = {}

    for char in text1_clean:
        freq[char] = freq.get(char, 0) + 1
    for char in text2_clean:
        freq[char] = freq.get(char, 0) - 1
    for val in freq.values():
        if val != 0:
            print(f"--> The words {text1} & {text2} are not Anagram.")
            return False
    print(f"--> The words {text1} & {text2} are Anagram")
    return True