#############################
#Program 1 Random Writer
#Daniel Jaffe
#7/1/24
#############################

#Import libraries
from random import randint, choice

#Debug function
Debug = False

#############
#Functions
#############

# returns a random seed of length level (or k) from the book
def get_seed():
    # pick a random index that represents the beginning of the seed in the book
    start = randint(0, len(book) - level)

    if Debug == True:
        print("start", start)
        print("level", level)
        print('book[start]', book[start])
        print("book[start:start+level]", book[start:start+level])

    # return the random seed of length level (or k)
    return book[start:start+level]

# returns a random next character given a seed from the book
def get_next_char(book,seed):
    # initialize the list of characters
    character_array = []

    # initialize the current index (where we begin to look in the book)
    new_start = book.find(seed)

    if Debug == True:
        print("new_start", new_start)

    # continually find the seed in the book
    for i in range(new_start,len(book)-level):
        # abort if the seed is not found (or it's at the end of the book)
        if book[i:i + level] != seed:
            continue

        # otherwise, add the next character to the list
        else:
            character_array.append(book[i+level])
            if Debug == True:
                print('book[i:i + level]', book[i:i + level])
                print('character_array', character_array)

    # if there is at least one next character in the list of characters, return a randomly chosen one
    if len(character_array) > 0:
        # choose character from list
        newchar = choice(character_array)
        if Debug == True:
            print('newchar', newchar)
        return newchar

    # otherwise, return some appropriate trigger (e.g., None)
    else:
        return None

######
# MAIN
######

# grab command line arguments (or manually set the parameters)
#  k (or level) -> the level of analysis performed on the book
#  length -> the length of output to generate
#  filename -> the filename that contains the text of the book
level = 1
length = 150
filename = "hg-wells_the-time-machine.txt"

# grab the book
with open(filename, "r") as f:
    book = f.read()

if Debug == True:
    print(book)

# initialize the output
sentence = ""

# pick a random seed of length level (or k)
seed = get_seed()

#adds seed to the output
sentence += seed

if Debug == True:
    print('sentence',sentence)
    print("get_next_char",get_next_char)
    print("seed",seed)

# repeat as long as there isn't enough output yet
while len(sentence) < length:
    # get a random next character
    next_char = get_next_char(book,seed)

    # if one exists
    if next_char != None:
        # add it to the output
        sentence += next_char
        if Debug == True:
            print("sentence",sentence)
            print("len(seed)",len(seed))
        # # and recalculate the seed
        seed = seed[1:len(seed)]+ next_char
        if Debug == True:
            print("new_seed",seed)
    # otherwise, pick another random seed
    elif next_char == None:
        seed = get_seed()
        if Debug == True:
            print("reset is true",seed)

# display the output
print(sentence)