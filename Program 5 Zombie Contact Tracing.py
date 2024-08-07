#########################
# Program 5 Zombie contact tracing
# Daniel Jaffe
# Date created: 7/31/24
#########################

# Imports
from CSC201UT import *

Debug = True

# Part 1
# I used a array since tranversing to through a array has a O(n)
def contact_with(first_name_array,contact_array):

    print("Contact records:")



    # loop through each line
    # Connect first name with contacts
    for i in range(0,len(first_name_array)):
        print(f"  {first_name_array[i]} had contact with {", ".join(contact_array[i])}")

# I choose a link list since it is a small data set but it is unpredictable
def patient_zeros(set1):
    pass

# Main
#######

with open("DataSet1.txt","r") as file:
    set1 = file.read().splitlines()

if Debug == True:
    print(set1)

# initialize arrays
people_array = []
first_name_array = []
contact_array = []

# loop through each line in the set
for line in (set1):

    # Split into arrays for first name and contacts
    people = line.split(",")
    people_array.append(people)
    first_name_array.append(people[0])
    contact_array.append(people[1:])
    contact_array.sort()

    if Debug == True:
        print("people", people)

if Debug == True:
    print("people_array", people_array)
    print("first_name_array", first_name_array)
    print("contact_array", contact_array)

# Part 1 Who did each sick person have contact with
contact_with(first_name_array,contact_array)

# Part 2 Who are patient zeros
patient_zeros()