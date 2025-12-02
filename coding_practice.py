def largest(nums_list):
    """
    Returns the largest number within the list
    """

    largest_so_far = nums_list[0]
    for i in nums_list:
        if i > largest_so_far:
            largest_so_far = i
    
    print("--> Largest Number in the list: ", largest_so_far)
    return largest_so_far

def smallest(nums_list):
    """
    Find the smallest number within the list
    """
    smallest_so_far = nums_list[0]
    for nums in nums_list:
        if nums < smallest_so_far:
            smallest_so_far = nums
    
    print("--> Smallest Number in the List: ", smallest_so_far)
    return smallest_so_far

def find_min_and_max(nums_list):
    """
    The functions finds both Min and Max in the numbers list.
    """

    min_num = nums_list[0]
    max_num = nums_list[0]
    for nums in nums_list:
        if nums < min_num:
            min_num = nums
        if nums > max_num:
            max_num = nums
    
    print(f"--> The Min and Max in the list are: ({min_num,max_num})")
    return min_num, max_num

def remove_duplicates(nums_list):
    """
    Remove Duplicates from the list
    """
    unique_list=[]
    for num in nums_list:
        if num not in unique_list:
            unique_list.append(num)
        
    print("--> No Duplicates List: ",unique_list)
    return unique_list

def reverse_list(nums_list):
    """
    Reverse a given numbers list without using built in reverse()
    """
    reversed_list = []
    for num in nums_list[::-1]:
        reversed_list.append(num)

    print("--> List in reverse order: ",reversed_list)
    return reversed_list

def second_largest(nums_list):
    """
    Finds the second largest number in the list
    """
    max_num = nums_list[0]
    second_max_num = nums_list[1]

    for num in nums_list:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num

    print("--> Max Number is: ", max_num)
    print("--> Second Largest Number is: ", second_max_num)
    return second_max_num

def num_count(nums_list):
    """
    Counts the occurrences of the numbers in the nums list.
    """
    counts = {}
    for num in nums_list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    print("--> Counts: ", counts)
    return counts

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

def is_anagram(text1, text2):
    """
    This function checks if the following two text1 & text2 are anagrams.
    
    :param text1: String input
    :param text2: String input
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

def reverse_vowel(text1, text2):
    

largest([150,20,30,3,5,23,100])
smallest([150,20,30,3,5,23,100])
find_min_and_max([150,20,30,3,5,23,100])
remove_duplicates([150,20,30,3,5,5,150,20,100])
reverse_list([2,3,20,30,45,100,150])
second_largest([150, 20, 30, 3, 300, 20, 100])
num_count([4,2,4,3,2,4])
count_vowels("Player")
is_palindrome("RaceCar")
is_anagram("Hello", "World")