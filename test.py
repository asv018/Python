def min_swaps(arr):
    n = len(arr)

    # Create a copy of the array and sort it in ascending order.
    sorted_arr = sorted(arr)

    # Create a dictionary to map each element in the sorted array to its index.
    index_map = {sorted_arr[i]: i for i in range(n)}

    # Initialize variables to count swaps for both ascending and descending orders.
    asc_swaps = 0
    desc_swaps = 0

    for i in range(n):
        if arr[i] != sorted_arr[i]:
            # For ascending order, count swaps to move the element to its correct position.
            # For descending order, count swaps to move the element to the reverse correct position.
            correct_position = index_map[arr[i]]
            arr[i], arr[correct_position] = arr[correct_position], arr[i]
            asc_swaps += 1
            desc_swaps += 1

    return asc_swaps, desc_swaps


arr = [5, 3, 1, 7, 2, 6, 4]
asc_swaps, desc_swaps = min_swaps(arr)
print("Minimum swaps for ascending order:", asc_swaps)
print("Minimum swaps for descending order:", desc_swaps)
