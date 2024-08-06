#########################
# Program 5 Zombie contact tracing
# Daniel Jaffe
# Date created: 7/31/24
#########################

from CSC201UT import *

Debug = True

# Part 1
# Used an unorder list since we had a small amount of data and amount of data was predictable
def contact_with(set1):

    for i in range (len(set1)):
        print(i)

    # output of each contact person 1 is in contact with
    print(f"{set1[0]} had contact with {set1[1:]}")









#######
# Main
#######

with open("DataSet1.txt","r") as file:
    set1 = file.read().split('\n')

if Debug == True:
    print(set1)


# outputs who each person had contact with
contact_with(set1)