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
    # output of start number
    # output of level
    # output of book starting point
    # output of book string starting point to starting point plus level
    if Debug == True:
        print("start", start)
        print("level", level)
        print('book[start]', book[start])
        print("book[start:start+level]", book[start:start+level])
    # return the random seed of length level (or k)
    return book[start:start+level]
# returns a random next character given a seed from the book
def get_next_char():
    # initialize the list of characters
    char_location_array = []
    # initialize the current index (where we begin to look in the book)
    i = start
    #output the length of the book
    if Debug == True:
        print("len(book)", len(book))
    # continually find the seed in the book
    while i < len(book):
        # find the index of the seed in the book beginning at the current index
        if str(book[i]) == str(book[start]):
            char_location_array.append(i)
            i += 1
            continue
        # abort if the seed is not found (or it's at the end of the book)
        else:
            i +=1

    #output char_array
    if Debug == True:
        print("char_array",char_location_array)

    # randomly choose the next character from the list
    random_location_start = choice(char_location_array)
    newchars = book[random_location_start+1:random_location_start+level+1]
    #output newchar
    #output random location start
    if Debug == True:
        print('newchars',newchars)
        print("output random location start", random_location_start)
    # and update the index in the book

    # if there is at least one next character in the list of characters, return a randomly chosen one
    if newchars:
        return newchars
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
level = 25
length = 150
filename = "hg-wells_the-time-machine.txt"

# grab the book
with open(filename, "r") as f:
    book = f.read()

#output of book
if Debug == True:
    print(book)

# initialize the output
sentence = ""

# picks a random starting point in the book
# pick a random seed of length level (or k)
start = randint(0, len(book) - level)
seed = get_seed()
sentence += seed
if Debug == True:
    print('sentence',sentence)
    #outputing get_next_char
if Debug == True:
    print("get_next_char",get_next_char)
# repeat as long as there isn't enough output yet
while len(sentence)+level <= length:
    # get a random next character
    next_char = get_next_char()
    # if one exists
    if next_char != None:
        # add it to the output
        sentence += next_char
        #output the sentence
        if Debug == True:
            print("sentence",sentence)
        # and recalculate the seed
        seed = get_seed()
    # otherwise, pick another random seed
    elif next_char == None:
        seed = get_seed()

# display the output
print(sentence)