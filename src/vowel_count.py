def count_vowels(text):
    """
    This function counts vowels in a given text input.
    """
    # Empty String Validation
    if len(text) == 0:
        raise ValueError("Cannot count vowels for empty string")
    count = 0
    for i in text.lower():
        if i in 'aeiou':
            count += 1

    print(f"--> The Vowel Count for the word {text}: ", count)
    return count

count_vowels("Player")
