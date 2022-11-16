import random

def linear_search(list1,target):
    """ Returns index position of target if found, else returns None"""
    
    # looping trough all the elements/items in the list
    for i in range(0,len(list1)):
        # looking if the item is equal to the target that we are looking for
        if list1[i]== target:
            # if it is we return the item
            return i
    # else we return None(nothing)
    return None

# testing if is working with list.
def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers,6)
verify(result)
