# Write a Python function that checks whether a passed string is palindrome or not.

def palindrome(s):

    s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]   # Check through slicing
