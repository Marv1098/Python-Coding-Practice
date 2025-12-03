def is_palindrome(text):
   """
   This function check if a given input is a palindrome or not
   """
   text = text.lower()
   left = 0
   right = len(text) - 1
   while left < right:
       if text[left] != text[right]:
           print(f"--> The word {text} is not a Palindrome")
           return False
       else:
           left += 1
           right -= 1
   print(f"--> The word {text} is a Palindrome")
   return True

is_palindrome("RaceCar")
