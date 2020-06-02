# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
