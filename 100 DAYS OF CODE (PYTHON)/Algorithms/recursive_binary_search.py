
def recursive_binary_search(list1, target):
    """recursive binary search does not return the index position of the target, but instead return TRUE if the target is in the list list or FALSE if the target does not exist in the list"""

    if len(list1) == 0:
        return False
    else:
        midpoint = (len(list1))//2

        if list1[midpoint] == target:
            return True
        else:
            if list1[midpoint] < target:
                return recursive_binary_search(list1[midpoint+1:], target)
            else:
                return recursive_binary_search(list1[:midpoint], target)



def verify(result):
    print(f"Target found: {result}")





numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)


result = result = recursive_binary_search(numbers, 6)
verify(result)


