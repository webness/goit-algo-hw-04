import random
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def test_sorts(array_size):
    array = [random.randint(1, 10000) for _ in range(array_size)]

    insertion_time = timeit.timeit(lambda: insertion_sort(array.copy()), number=1)

    merge_time = timeit.timeit(lambda: merge_sort(array.copy()), number=1)

    timsort_time = timeit.timeit(lambda: sorted(array.copy()), number=1)

    print(f"Array size: {array_size}")
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print(f"Timsort (Python's sorted) Time: {timsort_time:.6f} seconds")
    print()


for size in [100, 1000, 10000]:
    test_sorts(size)
