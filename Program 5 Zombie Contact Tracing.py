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
# I used an ordered array since transversing to through a array has a O(n)
def contact_with(set1):

    # initialize arrays
    people_array = []
    people_array_sorted = []
    first_name_array = []
    contact_array = []
    contact_array_sorted = []

    # loop through each line in the set
    for line in (set1):
        # Split into arrays for first name and contacts
        people = line.split(",")

    # Add all people into one array
        people_array.append(people)
        people_array_sorted.append(people)

    # sort people by first name
    for i in people_array:
        people_array_sorted.sort()

    # the first name from each array
    for i in range(len(people_array)):
        first_name_array.append(people_array[i][0])

    # First Name sorted alphabetically
    # Learned this function on W3Schools
    first_name_array_sorted = sorted(first_name_array)

    # the contacts of each first name
    # Remove the space from the last name
    for people in range(len(people_array_sorted)):
        people_array_sorted[people][-1] = (people_array_sorted[people][-1].strip())
        contact_array.append(people_array_sorted[people][1:])

    # sort contacts alphabetically
    for i in range(len(contact_array)):
        contact_array_sorted.append(sorted(contact_array[i]))

    if Debug == True:
        print("people_array", people_array)
        print("people_array_sorted",)
        print("first_name_array", first_name_array)
        print("first_name_array_sorted", first_name_array_sorted)
        print("contact_array", contact_array)
        print("contact_array_sorted", contact_array_sorted)


    print("Contact records:")
    # loop through each line
    # Connect first name with contacts
    for i in range(0,len(first_name_array_sorted)):
        print(f"  {first_name_array_sorted[i]} had contact with {", ".join((contact_array_sorted[i]))}")

    return(contact_array,first_name_array,people_array)

# Part 2
# I used an array to transverse through the all the people since it has O(n) and to search I used a binary tree for the contacts since it is a O(log2n) for a total O(nlog2n)
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
    # Then append to patient zero array
    for person in total_people_array:
        if search(contact_tree,person) == None:
            patient_zeros.append(person)

    if Debug == True:
        print("patient_zeros", patient_zeros)

    # sort patient zeros alphabetically
    patient_zeros.sort()

    # Output of patient zeros
    print(f"Patient zeros: {", ".join(patient_zeros)}")

    return total_contact_array,total_people_array, patient_zeros

# Part 3
# I used an array to transverse the contact names since it has O(n) and to search I used a binary tree for the first names since it is a O(log2n) for a total O(nlog2n)
def potential_zombies(first_name_array,total_contact_array):

    # Initializing values
    potential_zombies = []

    # Binary tree for all first Names
    first_name_tree = OrderedBinaryTree()
    for first_name in range(len(first_name_array)):
        first_name_tree.insert(first_name_array[first_name])

    if Debug == True:
        print("first_name_array", first_name_array)
        print("total_contact_array", total_contact_array)
        print(first_name_tree)

    # Search for the contact in firstname tree
    for contact in total_contact_array:
        if search(first_name_tree,contact) == None:
            potential_zombies.append(contact)

    if Debug == True:
        print("potential zombies", potential_zombies)

    # sort potential Zombies
    potential_zombies.sort()

    # Output of potential zombies
    print(f"Potential Zombies: {", ".join(potential_zombies)}")

    return potential_zombies

# Part 4
# I used an array to transverse the all people names since it has O(n) and to search I used a binary tree for the zombies and zeros since it is a O(log2n) for a total O(nlog2n)
def neither_zeros_or_zombies(total_people_array,patient_zeros,potential_zombies):

    # initializing values
    neither_zeros_or_zombies = []
    zeros_plus_zombies = potential_zombies + patient_zeros


    # Binary tree for zeros and zombies
    zeros_plus_zombies_tree = OrderedBinaryTree()
    for i in range(len(zeros_plus_zombies)):
        zeros_plus_zombies_tree.insert(zeros_plus_zombies[i])

    if Debug == True:
        print(zeros_plus_zombies_tree)
        print(zeros_plus_zombies)

    # loop through all people
    for person in total_people_array:

        # If person a patient zeros or potential zombie append to list
        if search(zeros_plus_zombies_tree, person) == None:
            neither_zeros_or_zombies.append(person)

    #Sort neither zeros or zombies alphabetically
    neither_zeros_or_zombies.sort()

    #output of neither zeros or zombies
    print(f"Neither patient zero nor potential zombie: {", ".join(neither_zeros_or_zombies)}")

# Main
#######

with open("DataSet1.txt","r") as file:
    set1 = file.readlines()

if Debug == True:
    print(set1)

# Part 1 Who did each sick person have contact with
contact_array, first_name_array, people_array = contact_with(set1)

# adding a new line
print()

# Part 2 Who are patient zeros
total_contact_array,total_people_array, patient_zeros = patient_zeros(people_array, contact_array)

# Part 3 Who are potential zombies
potential_zombies = potential_zombies(first_name_array,total_contact_array)

# Part 4 Who are neither patient zeros nor potential zombies
neither_zeros_or_zombies(total_people_array,patient_zeros,potential_zombies)