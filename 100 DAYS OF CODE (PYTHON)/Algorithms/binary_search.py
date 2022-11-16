def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        # for integer get result
        mid = (high + low) // 2

        # check if n is present at mid
        if list1[mid] < n:
            low = mid + 1

            # if n is greater, compare to the right of mid
        elif list1[mid] > n:
            high = mid - 1
        # if n is smaller, compared ot the left of mid
        else:
            return mid
    # element was not present in the list, return None
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


# this is already sorted, but in another case we will have to sort the list before we can implement the binary search.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 10)
verify(result)
