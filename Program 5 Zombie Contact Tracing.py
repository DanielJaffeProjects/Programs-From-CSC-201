#########################
# Program 5 Zombie contact tracing
# Daniel Jaffe
# Date created: 7/31/24
#########################

# Imports
from CSC201UT import OrderedBinaryTree

Debug = False


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


# Finds the highest numbers in the array
# outputs the highest numbers indexes
def find_high(array):
    # initializing values
    biggest_value = [0]
    indexes = []

    # loop through the entire array
    for i in range(len(array)):

        # if biggest value is greater than array
        # indexes becomes new index of biggest number
        # the biggest value becomes new biggest number
        if biggest_value[0] < array[i]:
            indexes = []
            biggest_value = []
            indexes.append(i)
            biggest_value.append(array[i])
        elif biggest_value[0] == array[i]:
            indexes.append(i)

    return indexes

    # Finds how much each name is in the contacts


def most_names(array_of_names):
    # Initializing values
    counter = 1
    counter_array = []

    # loop through all names
    for i in range(1, len(array_of_names)):

        # if array name is equal to previous name
        if array_of_names[i] == array_of_names[i - 1]:
            # then add one to the add one to the counter
            counter += 1

        else:
            # otherwise append counter to
            counter_array.append(counter)
            # reset the counter to one
            counter = 1

    # for the last value
    counter_array.append(counter)

    return (counter_array)


# count the -1 in array
def count_negative_one(array1):
    # initialize counter
    counter = 0
    # loop through array
    for i in array1:
        # if array in array is -1
        if i == [-1]:
            # then add 1 to counter
            counter += 1
    # return counter
    return counter


# Part 1
# I used an ordered array since transversing to through a array has a O(n)
def contact_with(data_set):
    # initialize arrays
    people_array = []
    people_array_sorted = []
    first_name_array = []
    contact_array = []
    contact_array_sorted = []

    # loop through each line in the set
    for line in (data_set):
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
        print("people_array_sorted", people_array_sorted)
        print("first_name_array", first_name_array)
        print("first_name_array_sorted", first_name_array_sorted)
        print("contact_array", contact_array)
        print("contact_array_sorted", contact_array_sorted)

    print("Contact records:")
    # loop through each line
    # Connect first name with contacts
    for i in range(0, len(first_name_array_sorted)):
        print(f"  {first_name_array_sorted[i]} had contact with {", ".join((contact_array_sorted[i]))}")

    return (contact_array, first_name_array, people_array)


# Part 2
# I used an array to transverse through the all the people since it has O(n) and to search I used a binary tree for the contacts since it is a O(log2n) for a total O(nlog2n)
def patient_zeros(people_array, contact_array):
    # Initializing values
    total_contact_array = []
    patient_zeros = []
    total_people_array = []

    # used geeks for geeks to combine contact array into one single array
    for i in sum(contact_array, []):
        if i not in total_contact_array:
            total_contact_array.append(i)

    # Combines all people into on array
    # removes duplicates
    for i in sum(people_array, []):
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
        if search(contact_tree, person) == None:
            patient_zeros.append(person)

    if Debug == True:
        print("patient_zeros", patient_zeros)

    # sort patient zeros alphabetically
    patient_zeros.sort()

    # Output of patient zeros
    print(f"Patient zeros: {", ".join(patient_zeros)}")

    return total_contact_array, total_people_array, patient_zeros


# Part 3
# I used an array to transverse the contact names since it has O(n) and to search I used a binary tree for the first names since it is a O(log2n) for a total O(nlog2n)
def potential_zombies(first_name_array, total_contact_array):
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
        if search(first_name_tree, contact) == None:
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
def neither_zeros_or_zombies(total_people_array, patient_zeros, potential_zombies):
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

    # Sort neither zeros or zombies alphabetically
    neither_zeros_or_zombies.sort()

    # output of neither zeros or zombies
    print(f"Neither patient zero nor potential zombie: {", ".join(neither_zeros_or_zombies)}")


# Part 5
# I used an array since I need to transverse through the entire list to see how many contacts each person had this gave me a O(n).
# I used find_high to find the highest index of the most contacts and then found the person in people array which gave me a big O(n) for a total of O(n)
def viral_people(people_array):
    # initializing values
    sizes_of_contact_list = []
    most_viral = []

    # Loops through people and appends size of contact list too arr
    for i in people_array:
        sizes_of_contact_list.append(len(i) - 1)

    # who has the most contacts
    indexes_of_most_contacts = find_high(sizes_of_contact_list)

    # The most viral people
    for i in indexes_of_most_contacts:
        most_viral.append(people_array[i][0])

    if Debug == True:
        print("sizes_of_contact_list", sizes_of_contact_list)
        print("indexes_of_most_contacts", indexes_of_most_contacts)
        print("people_array", people_array)
        print("most_viral", most_viral)

    # Most viral alphabetically
    most_viral.sort()

    # output the people with the most contacts
    print(f"Most viral people: {", ".join(most_viral)}")


# Part 6
# I used an array since I need to transverse through the entire list to see how many people where contacted by each sick person had this gave me a O(n).
# I used find_high to find the highest index of the most contacted people and then found the people in total_contact_array which gave me a big O(n) for a total of O(n)
def contact_people(contact_array, total_contact_array):
    # initializing values
    most_contacted = []
    all_contacts = sum(contact_array, [])

    # sort contacts alphabetically
    all_contacts.sort()
    total_contact_array.sort()

    # loop through all names and count how many of each name there are
    counts_of_contacts = most_names(all_contacts)

    # find which indexes had the most contacted
    indexes_highest_num_contacted = find_high(counts_of_contacts)

    # The most contacted people
    for i in indexes_highest_num_contacted:
        most_contacted.append(total_contact_array[i])

    if Debug == True:
        print("all_contacts", all_contacts)
        print("indexes_contacts", counts_of_contacts)
        print("most_contacts", most_contacted)
        print("indexes_highest_num_contacted", indexes_highest_num_contacted)
        print("total_contact_array", total_contact_array)

    # output the people who were most contacted by a sick person
    print(f"Most contacted people: {", ".join(most_contacted)}")


# Part 7
# I decide to use an array since I need to transverse through the contacts array and then through each separate array
# This gave me a O(n^2)
def max_distance_from_potential_zombie(first_name_array, contact_array, distance_values, distance_names, num):
    # initializing values
    removable = []
    removable_without_duplicate = []
    number_of_neg = []
    getting_remove = []
    previous_contact_array = count_negative_one(contact_array)

    # loop through all contacts arrays
    for i in contact_array:
        # loop through all array
        for number in i:
            # if number is -1 append it to array of negatives
            if number == -1:
                number_of_neg.append(number)
                # if number of negative is equal to the length of the array
                if len(number_of_neg) == len(contact_array):
                    # then all contacts have been searched through
                    return (distance_names, distance_values)

    # loop through all contacts
    for contacts in contact_array:
        # loop through people in those contacts
        for people in contacts:
            # if people in contacts are in distance names then add people to removable array
            if people in distance_names:
                removable.append(people)

    # remove the duplicates
    for i in removable:
        if i not in removable_without_duplicate:
            removable_without_duplicate.append(i)

    # Transverse through contacts in contact array
    for contacts in contact_array:
        # loop through contacts
        for people in contacts:
            # if person in contacts is in removable array
            if people in removable_without_duplicate:
                # add this to getting remove array in the front
                getting_remove.insert(0, people)

    # loop through the contacts
    for contacts in contact_array:
        # loop through people
        for i in getting_remove:
            # if person is in contacts remove them
            if i in contacts:
                contacts.remove(i)

    count_contact_array = str(count_negative_one(contact_array))
    previous_contact_array_count = str(previous_contact_array)

    # if contact array has been change
    if str(previous_contact_array) == str(count_negative_one(contact_array)) != True:
        # increase num by one
        num += 1
        # loop through contact array
        for i in range(len(contact_array)):
            # if contact_array is empty
            if contact_array[i] == []:
                # then append -1 to contacts array
                contact_array[i].append(-1)
                # and append value to distance value array
                distance_values.append((num))
                # add appends name to distance name array
                distance_names.append(first_name_array[i])

    if Debug == True:
        print("previous_contact_array", previous_contact_array)
        print("contact_array", contact_array)
        print("count_negative_one", count_negative_one(contact_array))
        print("count_negative_one", (previous_contact_array))

    if Debug == True:
        print("potential_zombies", potential_zombies)
        print("distance_names", distance_names)
        print("distance_values", distance_values)
        print("contact_array", contact_array)

    # recursion if base case has not been fulfilled
    return max_distance_from_potential_zombie(first_name_array, contact_array, distance_values, distance_names, num)


# Extra credit 1
# I used an array since I want to transverse through the entire contact list to see if they are a subset of potential zombies this gave me O(n)
def spreader_zombies(first_name_array, people_array, potential_zombies):
    # initializing values
    spreader_zombie_array = []

    #  loop through len of people array
    for i in range(len(people_array)):

        # find who are the contacts
        contact_array = people_array[i][1:]

        # looked up how to use set and subset on W3School
        if set(contact_array).issubset(set(potential_zombies)):
            spreader_zombie_array.append(first_name_array[i])

    # sort spreader zombie alphabetically
    spreader_zombie_array.sort()

    # output the spreader zombies
    print("  Spreader zombies:", ", ".join(spreader_zombie_array))


#######
# Main
#######

with open("DataSet5.txt", "r") as file:
    data_set = file.readlines()

if Debug == True:
    print(data_set)

# Part 1 Who did each sick person have contact with
contact_array, first_name_array, people_array = contact_with(data_set)

# adding a new line
print()

# Part 2 Who are patient zeros
total_contact_array, total_people_array, patient_zeros = patient_zeros(people_array, contact_array)

# Part 3 Who are potential zombies
potential_zombies = potential_zombies(first_name_array, total_contact_array)

# Part 4 Who are neither patient zeros nor potential zombies
neither_zeros_or_zombies(total_people_array, patient_zeros, potential_zombies)

# Part 5 Who are the most viral people
viral_people(people_array)

# Part 6 Who are the most contacted people
contact_people(contact_array, total_contact_array)

# adding a new line
print()

# Part 7 What is each person's maximum distance from a potential zombie
# initializing values
distance_names = []
distance_values = []
num = 0
new_contact_array = []
name_and_distance = []

# add potential zombies to array of name and values = 0
for zombie in potential_zombies:
    distance_names.append(zombie)
    distance_values.append(num)

# making new contact array
for i in range(len(people_array)):
    new_contact_array.append(people_array[i][1:])

distance_names, distance_values = max_distance_from_potential_zombie(first_name_array, new_contact_array,
                                                                     distance_values, distance_names, num)

print("Maximum distance from a potential zombie:")

# append distance names and value into one array
for i in range(len(distance_values)):
    name_and_distance.append([distance_names[i], distance_values[i]])

# sort by values then name
# used stack overflow to understand how to sort the values before the names
name_and_distance = sorted(name_and_distance, key=lambda x: x[1], reverse=True)

# loop through the array of names and distances
for i in range(len(name_and_distance)):
    # output maximum distance for each person
    print(f"  {name_and_distance[i][0]}: {name_and_distance[i][1]}")

# add an extra line
print()

# For extra credit
# Spreader Zombies
print("For extra credit:")
spreader_zombies(first_name_array, people_array, potential_zombies)
