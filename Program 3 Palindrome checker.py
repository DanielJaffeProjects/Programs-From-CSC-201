############
# Program 3 Palidrome checker
# Daniel Jaffe
# Date created: 7/17/24
############

# Import Functions
from CSC201UT import Deque

#Debugger
Debug = False

# Checks if palindrome
def isPalindrome(word):
    dq = Deque()

    # Lowercases the word
    word = word.lower()


    for letter in word:
        # If letter not alphabetical then skip
        if not letter.isalpha():
            continue
        # Otherwise add to the deque
        else:
            dq.add_rear(letter)

    if Debug == True:
        print(dq)

    # Checks if the first letter is the same as the last letter
    while (dq.size() > 1):
        if (dq.remove_front() != dq.remove_rear()):
            return False

    return True

#######
# Main
#######

# opening the palindrome text
with open("phrases.txt","r") as f:
    phrases = f.readlines()

if Debug == True:
    print(phrases)

# Go through each phrase and check if palindrome
for phrase in phrases:
    if (isPalindrome(phrase)) == True:
        print(f"{phrase.strip()} Is a palindrome.")
