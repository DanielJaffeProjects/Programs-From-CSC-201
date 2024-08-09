#########################
# Program 5 Zombie contact tracing
# Daniel Jaffe
# Date created: 7/31/24
#########################

# Imports
from CSC201UT import OrderedBinaryTree

Debug = True

# Added search function for binary tree
def search(tree, val):
    Node = tree._root
    while Node:
        if Node._value == val:
            return Node
        elif val < Node._value:
            Node = Node._left
        else:
            Node = Node._right
    return None

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
        # Split into arrays for first name and contacts
        people = line.split(",")

    # Add all people into one array
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
# I used a array to tranverse since it has O(n) and to search I used a binary tree since it is a O(log2n) for a total O(nlog2n)
def patient_zeros(people_array,contact_array):

    # Initializing values
    total_contact_array = []
    patient_zeros = []
    total_people_array =[]

    # used geeks for geeks to combine contact array into one single array
    for i in sum(contact_array,[]):
        if i not in total_contact_array:
            total_contact_array.append(i)

    # Combines all people into on array
    # removes duplicates
    for i in sum(people_array,[]):
        if i not in total_people_array:
            total_people_array.append(i)

    # Binary tree for all contacts
    contact_tree = OrderedBinaryTree()
    for contact in range(len(total_contact_array)):
        contact_tree.insert(total_contact_array[contact])


    if Debug == True:
        print("total_contact_array", total_contact_array)
        print("people_array", people_array)
        print("contact_array", contact_array)
        print("total_people_array", total_people_array)
        print(contact_tree)


    # loop through all the people and compare to the contacts
    # Then append to pateint zero array
    for person in total_people_array:
        if search(contact_tree,person) == None:
            patient_zeros.append(person)

    if Debug == True:
        print("patient_zeros", patient_zeros)

    # Output people who are not in other contact list
    print(f"Patient zeros: {", ".join(patient_zeros)}")

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
patient_zeros(people_array, contact_array)
#
# # Part 3 Who are potential zombies
# potential_zombies(first_name_array,total_contact_array)
