#!/usr/bin/env python
# coding: utf-8

# STRING BASED PROBLEMS
# 

# 1.Write a Program to reverse a string

# In[6]:


def reverse_string(input_string):
    #Define a function called reverse_string that takes an input_string as its parameter.

    reversed_string = ""
    #Taking an empty string called reversed_string to store the reversed characters.

    for char in input_string:
        #Start a loop that iterates through each character in the input_string.

        reversed_string = char + reversed_string
        # Concatenate the current character with the existing reversed_string.
        # This effectively adds the current character to the beginning of the reversed string.

    return reversed_string
    #After the loop is done, return the reversed_string as the output of the function.
input_str = input()
reversed_str = reverse_string(input_str)
print(reversed_str)


# 2.Check if a string is a palindrome

# In[16]:


#define a function called palindrome by taking input_string as a argument
def palindrome(input_string):
    return input_string==input_string[::-1]
#Taking input from the user
input_string=input("enter a string:")
#It takes whether the given inpuit string is a palindrome or not
result=palindrome(input_string)
#This is just that it makes sure that everyletter is in lowercase to get correct output
cleaned_string=input_string.lower()

#loop to check and print the result
if result:
    print("Is a palindrome")
else:
    print("Not a palindrome")
    


# 3.Convert a string to Uppercase
# 

# In[23]:


input_string=input("enter a string:")
uppercase=input_string.upper()
print("uppercase:",uppercase)


# 4.Convert a string to Lowercase
# 

# In[24]:


input_string=input("enter a string:")
lowercase=input_string.lower()
print("lowercase:",lowercase)


# 5.Count the number of vowels in string
# 

# In[27]:


#Taking the input sentence from user
input_string=str(input("Enter a string:"))
#Writing a function to count the vowels
def vowel_count(input_string):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in input_string:
        if alphabet in vowel:
            count=count+1
    #print the number the vowels
    print("No.of vowels :",count)
#return function
vowel_count(input_string)


# 6.Count the number of consonants in a string

# In[28]:


#Taking the input sentence from user
input_string=str(input("Enter a string:"))
#Writing a function to count consonants
def consonant_count(input_string):
    count=0
    consonant=set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    for alphabet in input_string:
        if alphabet in consonant:
            count=count+1
    #print the number the consonantss
    print("No.of consonants :",count)
#return function
consonant_count(input_string)


# 7.Remove all the whitespaces from string

# In[29]:


#Take input string
Input_string=" wa t er "
#Remove spaces
modified_string=Input_string.replace(" ","")
#Print the modified string 
print(modified_string)


# 8. Find the length of a string without using the len() function

# In[32]:


# Initialize a variable to keep track of the count
count = 0

# Iterate through each character in the string
for char in input_string:  # Replace 'input_string' with your actual string variable
# Increment the count variable by 1 for each character
    count += 1
input_string=input()

# Print the final count, which represents the length of the string
print("The length of the string is:", count)


# 9. Check if a string contains a specific word

# In[33]:


#Input the string and the specific word
input_string = input("Enter a string: ")
specific_word = input("Enter the specific word to check for: ")

#Check if the specific word is present in the string using the 'in' keyword
if specific_word in input_string:
    #Print message if word is present
    print(f"The string contains the word '{specific_word}'.")
else:
    #Print message if word is not present
    print(f"The string does not contain the word '{specific_word}'.")


# 10. Replace a word in a string with another word.

# In[2]:


input_string=input("enter a sentence:")
replace_word=input("enter a string:")
new_word=input("enter a string:")

modified_string=input_string.replace(replace_word,new_word)
print("modified string is",modified_string)


# 11. Count the occurrences of a word in a string.

# In[1]:


def count_word_occurrences(input_string, target_word):
    #Initialize a variable to keep track of the word count
    word_count = 0

    #Split the input string into a list of words
    words = input_string.split()

    # Iterate through each word in the list
    for word in words:
        #Check if the current word matches the target word
        if word == target_word:
            #Increment the word count if the words match
            word_count += 1

    #Return the final word count
    return word_count

# Input string
input_string = input()

# Target word to count
target_word = input()

# Call the function and print the result
result = count_word_occurrences(input_string, target_word)
print(f"The word '{target_word}' appears {result} times in the input string.")


# 12. Find the first occurrence of a word in a string.
# 

# In[2]:


#defining the function 
def first_occurence(text,word):
    #writing find function 
    index=text.find(word)
    #initialising a loop to make sure of all conditions are achieved
    if index==-1:
        return none
    
    return index
#taking input from user and applying the function     
text=input()
word=input()
result=first_occurence(text,word)
#print the result
print("first occurence is:",result)


# 13. Find the last occurrence of a word in a string.

# In[4]:


#defining the function 
def last_occurence(text,word):
    #writing find function 
    index=text.rfind(word)
    #initialising a loop to make sure of all conditions are achieved
    if index==-1:
        return none
    
    return index
#taking input from user and applying the function     
text=input()
word=input()
result=last_occurence(text,word)
#print the result
print("last occurence is:",result)


# 14. Split a string into a list of words.

# In[5]:


def split_into_words(text):
    #using split function to split the text and assigned it to variable
    list=text.split()
    return list
#Taking input from user and calling function and storing it in variable and printing the result
text=input()
result=split_into_words(text)
print(result)
    


# 15. Join a list of words into a string.

# In[14]:


def words_into_string(text):
    #as it is to combine we use join operator
    string=' '.join(text)
    return string
#Taking input calling function and print
text=["this", "is", "apple"]
result=words_into_string(text)
print(result)


# 16. Convert a string where words are separated by spaces to one where words are separated by underscores.

# In[16]:


def spaces_into_underscores(text):
    #as we have to replace space with underscore this is used
    modified=text.replace(" ",'_')
    return modified
#Taking input calling function and print
text="   th is"
result=spaces_into_underscores(text)
print(result)


# 17. Check if a string starts with a specific word or phrase.

# In[19]:


def starts_with(text,prefix):
    #used startswith function to check the condition
    start=text.startswith(prefix)
    return start
#here there are two inputs text and prefix and calls the function
text =input()
prefix=input()
result=starts_with(text,prefix)
#here if condition is used to print if that doesnot start with that particular prefix
if result:
    print("The text starts with the prefix.")
else:
    print("The text does not start with the prefix.")


# 18. Check if a string ends with a specific word or phrase.

# In[20]:


def ends_with(text,suffix):
    #used endwith function to check the condition
    end=text.endswith(prefix)
    return end
#here there are two inputs text and suffix and calls the function
text =input()
suffix=input()
result=starts_with(text,suffix)
#here if condition is used to print if that doesnot end with that particular suffix
if result:
    print("The text ends with the suffix.")
else:
    print("The text does not end with the suffix.")


# 19. Convert a string to title case (e.g., "hello world" to "Hello World").

# In[21]:


def string_to_title(text):
    #To convert text into title here we used title()
    logic=text.title()
    return logic
#Taking input calling function and print
text=input()
result=string_to_title(text)
print(result)


# 20. Find the longest word in a string.

# In[23]:


def longest_word(text):
    #To divide the text into individual words
    words=text.split()
    #initialising longet_word and maximum length
    longest_word=""
    max_len=0
    #for loop in order to check the length of words with maximum length iteratively.
    for word in words:
        if len(word)>max_len:
            max_len=len(word)
            longest_word=word
    return longest_word
#Taking input calling function and printing result
text=input()
result=longest_word(text)
print(result)


# 21. Find the shortest word in a string

# In[26]:


def shortest_word(text):
    #To divide the text into individual words
    words=text.split()
    #initialising longest_word and maximum length
    shortest_word=None
    min_len=float('inf')
    #for loop in order to check the length of words with maximum length iteratively.
    for word in words:
        if len(word)<min_len:
            min_len=len(word)
            shortest_word=word
    return shortest_word
#Taking input calling function and printing result
text=input()
result=shortest_word(text)
print(result)


# 22. Reverse the order of words in a string.

# In[3]:


# input string
string = input()
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
    # appending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))


# 23. Check if a string is alphanumeric.

# In[5]:


def is_alphanumeric(text):
    #Use the isalnum() method to check if the string is alphanumeric.
    return text.isalnum()

# Taking input from the user and storing the function in variable
text = input()
result = is_alphanumeric(text)
#loop to print the answer in all the possible cases
if result:
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")


# 24. Extract all digits from a string.

# In[11]:


#function to extract the digits
def extract_digits(string):
    #initialising the digits in order to store them.
    digits=""
    #using for loop for a string in order to check the presence of digits
    for char in string:
        if char.isdigit():
            digits+=char
    return digits
#usage example
string=input()
result=extract_digits(string)
print(result)


# 25. Extract all alphabets from a string.

# In[13]:


#function to extract the alphabets
def extract_alphabets(string):
    #initialising the digits in order to store them.
    alphabets=""
    #using for loop for a string in order to check the presence of digits
    for char in string:
        if char.isalpha():
            alphabets+=char
    return alphabets
#usage example
string=input()
result=extract_alphabets(string)
print(result)


# 26. Count the number of uppercase letters in a string.

# In[18]:


def count_uppercase(string):
    #one liner condition to check and return the count of uppercase charecters
    count=sum(1 for char in string if char.isupper())
    return count
#usage example
string=input()
result=count_uppercase(string)
print(result)            


# 27. Count the number of lowercase letters in a string.
# 
# 

# In[19]:


def count_uppercase(string):
    #one liner condition to check and return the count of uppercase charecters
    count=sum(1 for char in string if char.islower())
    return count
#usage example
string=input()
result=count_uppercase(string)
print(result)            


# 28. Swap the case of each character in a string.

# In[20]:


def swap_case(input_string):
    #in-built function to swap the cases
    swapped_string=input_string.swapcase()
    return swapped_string
#usage example
input_string=input()
result=swap_case(input_string)
print(result)


# 29. Remove a specific word from a string.
# 

# In[23]:


def remove_word(input_string,word_to_remove):
    words=input_string.split()
    filtered_words=[word for word in words if word!=word_to_remove]
    modified_word=''.join(filtered_words)
    return modified_word
#usage example
input_string=input()
word_to_remove=input()
result=remove_word(input_string,word_to_remove)
print(result)
    


# 30. Check if a string is a valid email address.

# In[28]:


#import regular expresiion module
import re 

def is_valid_email(email):
    #this pattern is to match the charecters for a valid email
    pattern= r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,email):
        return True
    else:
        return False
    #usage example
email=input()
result=is_valid_email(email)
print(result)
    
    


# 31. Extract the username from an email address string.

# In[30]:


def extract_username(email):
    #to get the useraname split the email at @ and get the first name
    username=email.split('@')[0]
    return username
#usage example
email=input()
result=extract_username(email)
print(result)


# 32. Extract the domain name from an email address string.

# In[31]:


def extract_domainname(email):
    #to get the useraname split the email at @ and get the first name
    domainname=email.split('@')[1]
    return domainname
#usage example
email=input()
result=extract_domainname(email)
print(result)


# 33. Replace multiple spaces in a string with a single space.
# 

# In[36]:


def replace_multiple_spaces(input_string):
    modified_string=' '.join(input_string.split())
    return modified_string
input_string=input()
result=replace_multiple_spaces(input_string)
print(result)


# 33. Replace multiple spaces in a string with a single space.
# 

# In[39]:


from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])  # Check if both scheme and netloc are present
    except ValueError:
        return False

# Example URLs
url1 = "https://www.dotnet.com"
url2=input()
result1 = is_valid_url(url1)
result2=is_valid_url(url2)
print(result1)  # Should print True
print(result2)


# 35. Extract the protocol (http or https) from a URL string.

# In[41]:


def extract_protocol(url):
    # Find the index of the first occurrence of "://"
    protocol_end = url.find("://")

    if protocol_end != -1:
        # Extract the protocol from the URL
        protocol = url[:protocol_end]
        return protocol
    else:
        return None

# Example URL strings
url1 = "http://google.com"
url2 = "ftp://ftp.example.com"

# Extract protocols
protocol1 = extract_protocol(url1)
protocol2 = extract_protocol(url2)

# Print extracted protocols
print("Protocol 1:", protocol1)
print("Protocol 2:", protocol2)

    


# 36. Find the frequency of each character in a string.
# 

# In[42]:


def character_frequency(input_string):
    frequency = {}  # Create an empty dictionary to store character frequencies

    for char in input_string:
        if char in frequency:
            frequency[char] += 1  # Increment the frequency count if the character is already in the dictionary
        else:
            frequency[char] = 1   # Initialize the frequency count to 1 if the character is not in the dictionary

    return frequency

# Example string
input_str = "hello world"

# Calculate character frequencies
char_freq = character_frequency(input_str)

# Print character frequencies
for char, freq in char_freq.items():
    print(f"Character: '{char}', Frequency: {freq}")


# 37. Remove all punctuation from a string.

# In[43]:


import string

def remove_punctuation(input_string):
    # Create a translation table to remove punctuation
    translator = str.maketrans("", "", string.punctuation)

    # Use the translation table to remove punctuation from the input string
    clean_string = input_string.translate(translator)

    return clean_string

# Example string with punctuation
input_str = "Hello, world! How's it going?"

# Remove punctuation
cleaned_str = remove_punctuation(input_str)

# Print the cleaned string
print("Original string:", input_str)
print("Cleaned string:", cleaned_str)


# 38. Check if a string contains only digits.

# In[51]:


def contains_only_digits(input_string):
    #in-built function to check if the string is digits or not
    return input_string.isdigit()
#usage example
input_string=input()
result=contains_only_digits(input_string)
print(f"'{input_string}'contains only digits:",result)


# 39. Check if a string contains only alphabets.

# In[52]:


def contains_only_alphabets(input_string):
    #in-built function to check if the string is alphabets or not
    return input_string.isalpha()
#usage example
input_string=input()
result=contains_only_alphabets(input_string)
print(f"'{input_string}'contains only alphabets:",result)


# 40. Convert a string to a list of characters.
# 

# In[53]:


def string_to_list(input_string):
    char_list=list(input_string)
    return char_list
#usage example
input_string=input()
result=string_to_list(input_string)
print(result)


# 41. Check if two strings are anagrams.

# In[55]:


def are_anagrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    
    return sorted(str1)==sorted(str2)
#usage example
str1="apple"
str2="gun"
result=are_anagrams(str1,str2)
print(f"'{str1}'and'{str2}'are anagrams:'",result)


# 42. Encode a string using a Caesar cipher.

# In[57]:


def caesar_cipher(text, shift):

  # Initialize an empty string to store the encoded text.
  encoded_text = ""

  # Iterate through each character in the input text.
  for char in text:
    # Check if the character is alphabetic.
    if char.isalpha():
      # Calculate the encoded character's Unicode code point value by shifting it by the specified amount.
      # Ensure the value wraps around within the lowercase alphabet range (a-z).
        encoded_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
    else:
      # Keep non-alphabetic characters unchanged.
      encoded_char = char

    # Add the encoded character to the encoded text.
    encoded_text += encoded_char

  # Return the resulting encoded text.
  return encoded_text

# Define the input text and the shift value for encoding.
text = "this is an example"
shift = 4

# Call the caesar_cipher function to encode the text using the specified shift.
encoded_text = caesar_cipher(text, shift)

# Print the encoded text.
print("Encoded text:", encoded_text)


# 43. Decode a Caesar cipher encoded string.

# In[59]:


def caesar_cipher_decoder(text, shift):
    
    # Initialize an empty string to store the decoded text
    decoded_text = ""

    # Loop through each character in the input text
    for char in text:
        # Check if the character is an alphabetic character
        if char.isalpha():
            # Calculate the decoded character using the shift value
            decoded_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            # If the character is not alphabetic, keep it unchanged
            decoded_char = char

        # Add the decoded character to the decoded text
        decoded_text += decoded_char

    # Return the fully decoded text
    return decoded_text
# Example input
text = "xlmw mw er ibeqtpi"
shift = 4

# Call the caesar_cipher_decoder function to decode the input text
decoded_text = caesar_cipher_decoder(text, shift)

# Print the decoded text
print("Decoded text:", decoded_text)


# 44. Find the most frequent word in a string.

# In[70]:


import re
from collections import Counter

def most_frequent_word(input_string):
    # Remove punctuation and convert to lowercase
    clean_string = re.sub(r'[^\w\s]', '', input_string).lower()

    # Split the string into words
    words = clean_string.split()

    # Use Counter to count word frequencies
    word_counter = Counter(words)

    # Find the most common word
    most_common_word = word_counter.most_common(1)[0][0]

    return most_common_word

# Example string
input_str = "the sky is as the skin"

# Find the most frequent word
most_common = most_frequent_word(input_str)

# Print the result
print("Most frequent word:", most_common)


# 45. Find all unique words in a string.

# In[73]:


import re

def unique_words(input_string):
    # Remove punctuation and convert to lowercase
    clean_string = re.sub(r'[^\w\s]', '', input_string).lower()

    # Split the string into words and convert to a set for uniqueness
    words = set(clean_string.split())

    return words

# Example string
input_str = "string is input string"

# Find unique words
unique_word_set = unique_words(input_str)

# Print the result
print("Unique words:", unique_word_set)


# 46. Count the number of syllables in a string.

# In[75]:


import re

def count_syllables(word):
    vowel_groups=re.findall(r'[aeiou]+',word,re.IGNORECASE)
    return len(vowel_groups)
word="name"
result=count_syllables(word)
print(f"'{word}' has {result} syllables.")


# 47. Check if a string contains any special characters.

# In[77]:


import re

def contains_special_characters(input_string):
    # Define a regular expression pattern to match special characters
    pattern = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/]')

    # Use the search() method to find a match
    match = pattern.search(input_string)

    # Return True if a match is found, False otherwise
    return bool(match)
#usage example
input_string="this is an example!"
result=contains_special_characters(input_string)
print(result)


# 48. Remove the nth word from a string.

# In[78]:


def remove_nth_word(input_string, n):
    # Split the input string into words
    words = input_string.split()

    # Check if n is within a valid range
    if n >= 1 and n <= len(words):
        # Remove the nth word by excluding it from the words list
        removed_word = words.pop(n - 1)

        # Join the remaining words to form the modified string
        modified_string = ' '.join(words)

        return modified_string, removed_word
    else:
        return None, None

# Example string and n value
input_str = "This is an example sentence to test the function."
n_value = 2

# Remove the nth word
modified_str, removed_word = remove_nth_word(input_str, n_value)

# Print the results
print("Original string:", input_str)
if modified_str is not None:
    print("Modified string:", modified_str)
    print("Removed word:", removed_word)
else:
    print("Invalid n value.")


# 49. Insert a word at the nth position in a string.

# In[80]:


#taking inputs of original string and string to be added and index
original_str="this sleepy dog"
add_str=" is a"
index=4
#using string slicing to add the string at exact position
result=f"{original_str[:index]}{add_str}{original_str[index:]}"
#print the result.
print(result)


# 50. Convert a CSV string to a list of lists.

# In[84]:


def csv_string_to_list(csv_string):
    #splitting it into single lines
    lines=csv_string.split('\n')
    #initialising an empty list 
    result=[]
    for line in lines:
        fields=line.split(',')
        result.append(fields)
    return result
#usage example
csv_data="Name,Age,Gender\nLeo, 35, M"
list_of_lists=csv_string_to_list(csv_data)
for row in list_of_lists:
    print(row)


# In[ ]:




