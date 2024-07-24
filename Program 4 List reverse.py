##################
# Program 4 List reverse
# Daniel Jaffe
# Date Created 7/24/24
###################

Debug = False

# reverses list
def reverse_list(lst):
    # if len of list is equal to or less than 1 return lst
    if len(lst) <= 1:
        return lst
    # Otherwise return first thing in list to the back
    else:
        return reverse_list(lst[1:]) + lst[:1]

#####
#Main
#####
# initialize the list
lst = []

# A list from 1 to 35 in integers
for i in range(1,36):
    lst.append(i)

if Debug == True:
    print(lst)

# Output the reversed list
print(reverse_list(lst))

