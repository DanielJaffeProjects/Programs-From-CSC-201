#########################
# Program 5 Zombie contact tracing
# Daniel Jaffe
# Date created: 7/31/24
#########################

# Imports
from CSC201UT import BinaryTree

Debug = True

# Part 1
# I used a array since tranversing to through a array has a O(n)
def contact_with(first_name_array,contact_array):

    print("Contact records:")

    # loop through each line
    # Connect first name with contacts
    for i in range(0,len(first_name_array)):
        print(f"  {first_name_array[i]} had contact with {", ".join(contact_array[i])}")

# Part 2
# Used a array since I need to tranverse the people array list to find and one that was not in anyone else contact list this gave me a O(n)
def patient_zeros(people_array,contact_array):

    # initialize patients zeros array
    patient_zeros = []

    # used geeks for geeks to combine contact array into one single array
    total_contact_array = sum(contact_array,[])

    if Debug == True:
        print(total_contact_array)
        print(people_array)
        print(contact_array)

    # loop through all the people and append people not in contact array
    for i in range(0,len(people_array)):
        if people_array[i] not in total_contact_array:
            patient_zeros.append(people_array[i])

    # Output people who are not in other contact list
    print("Patient zeros:",", ".join(patient_zeros))

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

    # removing duplicates in people array
    for i in people:
        if i not in people_array:
            people_array.append(i)

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
patient_zeros(people_array, contact_array)