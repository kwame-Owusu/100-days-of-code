

def binary_search(list1,target):
    # first item/element in the list
    first = 0
    # last item/elem in the list
    last = len(list1) - 1
    # only going to run if first item is less or equal to last item
    while first <= last:
        # adding first and last item and doing a floor division to return a whole number instead of a float
        midpoint = (first + last)//2
        # if the midpoint is equal to the target, we return the midpoint and end the loop.
        if  list1[midpoint] == target:
            return midpoint
        # if the midpoint is less that the target the first item will be midpoint + 1, so now we will be looking at the right side of the list.
        elif list1[midpoint] < target:
            first = midpoint  + 1 
        # else the last item becomes midpoint - 1, hence we will be looking in the left side of the list
        else:
            last = midpoint - 1
    return None



def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target  not found in list")   

# this list is ordered, but in any application of the binary search if the list is not sorted, it will not work, and return None even if the value we are looking for exist in the list
numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers,5)
verify(result)






