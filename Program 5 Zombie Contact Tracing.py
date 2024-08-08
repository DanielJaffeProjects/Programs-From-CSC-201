#########################
# Program 5 Zombie contact tracing
# Daniel Jaffe
# Date created: 7/31/24
#########################

# Imports
from binarysearchtree import TreeNode,BinarySearchTree

Debug = True

# Part 1
# I used an ordered array since tranversing to through a array has a O(n)
def contact_with(set1):

    print("Contact records:")

    # initialize arrays
    people_array = []
    first_name_array = []
    contact_array = []

    # loop through each line in the set
    for line in (set1):
        print(line)
        # Split into arrays for first name and contacts
        people = line.split(",")

        # first_name_array.append(people[0])
        # contact_array.append(people[1:])
        # contact_array.sort()
        people_array.append(people)

    # Sorts so that first name in people array is alphabetical
    people_array.sort()

    # the first name from each array
    for i in range(len(people_array)):
        first_name_array.append(people_array[i][0])

    # the contacts of each first name
    # Remove the space from the last name
    for people in range(len(people_array)):
        people_array[people][-1] = (people_array[people][-1].strip())
        contact_array.append(people_array[people][1:])

    # Sorting the contacts in alphabetical order
    for contact in (contact_array):
        contact.sort()

    if Debug == True:
        print("people_array", people_array)
        print("first_name_array", first_name_array)
        print("contact_array", contact_array)


    # loop through each line
    # Connect first name with contacts
    for i in range(0,len(first_name_array)):
        print(f"  {first_name_array[i]} had contact with {", ".join((contact_array[i]))}")

    return(contact_array,first_name_array,people_array)

# Part 2
#
def patient_zeros(people_array,contact_array):

    # Initializing values
    total_contact_array = []

    # initialize patients zeros array
    patient_zeros = []

    # used geeks for geeks to combine contact array into one single array
    for i in sum(contact_array,[]):
        if i not in total_contact_array:
            total_contact_array.append(i)


    if Debug == True:
        print(total_contact_array)
        print(people_array)
        print(contact_array)

    # loop through all the people and append people not in contact array
    for i in range(0,len(people_array)):

    if Debug == True:
        print("patient_zeros", patient_zeros)

    # Output people who are not in other contact list
    print(f"Patient zeros: {", ".join(patient_zeros)}")

    return(total_contact_array)
# # Part 3
# #
# def potential_zombies(first_name_array,total_contact_array):
#     for i in range(0,len(first_name_array)):
#         pass
# Main
#######

with open("DataSet1.txt","r") as file:
    set1 = file.readlines()

if Debug == True:
    print(set1)

# Part 1 Who did each sick person have contact with
contact_array,first_name_array,people_array = contact_with(set1)

# adding a new line
print()

# Part 2 Who are patient zeros
total_contact_array = patient_zeros(people_array, contact_array)
#
# # Part 3 Who are potential zombies
# potential_zombies(first_name_array,total_contact_array)