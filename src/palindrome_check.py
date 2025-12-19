def is_palindrome(text):
   """
   This function check if a given input is a palindrome or not
   """
   
   # Type Validation
   if not isinstance(text, (str, int)):
       raise TypeError("Input must be a string or integer.")
   
   # convert int to string
   text = str(text).lower()

   # Remove non-alphanumeric characters (space, punctuation, symbols)
   clean_text = ''.join(c for c in text if c.isalnum())

   # Empty input validation
   if not clean_text:
       raise ValueError("Input cannot be empty.")

   left = 0
   right = len(clean_text) - 1
   while left < right:
       if clean_text[left] != clean_text[right]:
           print(f"--> The input {text} is not a Palindrome")
           return False
       else:
           left += 1
           right -= 1
   print(f"--> The input {text} is a Palindrome")
   return True

is_palindrome(" ")
