def is_anagram(text1, text2):
    """
    This function checks if the following two text1 & text2 are anagrams.
    
    text1: String input
    text2: String input
    """

    text1_clean = text1.replace(" ", "")
    text2_clean = text2.replace(" ", "")

    if len(text1_clean) != len(text2_clean):
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

is_anagram("Hello", "World")