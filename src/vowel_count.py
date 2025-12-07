def count_vowels(text):
    """
    This function counts vowels in a given text input.
    """

    # Type Check
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    # Empty String Validation
    if len(text) == 0:
        raise ValueError("Cannot count vowels for empty string")
    
    # Non-alphabetic Validation
    if not text.isalpha():
        raise ValueError("Text must contain only alphabetic characters.")
    
    valid_vowels = 'aeiouAEIOU'
    accented_vowels = 'áéíóúÁÉÍÓÚ'

    # Accented Vowels Check
    if any(char in accented_vowels for char in text):
        raise ValueError("Accented vowels are not allowed.")
    
    count = 0
    for i in text:
        if i in valid_vowels:
            count += 1

    print(f"--> The Vowel Count for the word {text}: ", count)
    return count

count_vowels("Player")
