def count_vowels(text):
    """
    This function counts vowels in a given text input.
    """

    count = 0
    for i in text.lower():
        if i in 'aeiou':
            count += 1

    print(f"--> The Vowel Count for the word {text}: ", count)
    return count

count_vowels("Player")
