import heapq


def merge_k_lists(lists):
    # Initialize a min-heap to store the first element of each list along with the list index
    min_heap = []
    for index, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], index, 0))  # (value, list index, element index within list)

    merged_list = []

    # Extract the smallest element and add the next element from the same list to the heap
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)

        # Push the next element from the same list if it exists
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return merged_list


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Sorted list:", merged_list)
