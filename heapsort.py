import random
import time

# --- Heapsort ---
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# --- Quicksort ---
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    rest = arr[:pivot_index] + arr[pivot_index+1:]
    less = [x for x in rest if x <= pivot]
    greater = [x for x in rest if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)



# --- Merge Sort ---
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Timing Function ---
def time_algorithm(func, arr, in_place=False):
    arr_copy = arr.copy()
    start = time.time()
    if in_place:
        func(arr_copy)
    else:
        func(arr_copy)
    return time.time() - start

# --- Main Comparison ---
if __name__ == "__main__":
    sizes = [1000, 2000, 5000]
    input_types = ['random', 'sorted', 'reversed']

    for size in sizes:
        print(f"\n--- Array Size: {size} ---")
        arrays = {
            'random': [random.randint(0, 10000) for _ in range(size)],
            'sorted': list(range(size)),
            'reversed': list(range(size, 0, -1))
        }

        for input_type in input_types:
            test_arr = arrays[input_type]
            print(f"\nInput Type: {input_type.capitalize()}")

            hs_arr = test_arr.copy()
            hs_time = time_algorithm(heapsort, hs_arr, in_place=True)
            print(f"Heapsort Time:    {hs_time:.6f} seconds")

            qs_time = time_algorithm(quicksort, test_arr)
            print(f"Quicksort Time:   {qs_time:.6f} seconds")

            ms_time = time_algorithm(mergesort, test_arr)
            print(f"Merge Sort Time:  {ms_time:.6f} seconds")
