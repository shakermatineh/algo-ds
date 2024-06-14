import heapq
import os
import random


# outer loop on all elements i
# inner loop j reversed from last element to one right after i
# at the end of each inner loop, smallest element bubbles down at its final place.
# best case is O(n) when array sorted, use a flag to exit early. 
def bubble_sort(nums):
    """
    TC, SC = O(n^2), O(1)
    best, worst = O(n), O(n^2)
    stable: Yes. (original order of equal elements are maintained.)
    when to use: 
        * when array is nearly sorted. 
        * small array when simplicity beneficial.
        * memory constraint.
    """
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-1, i, -1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                swapped = True
        if not swapped:
            break
    return nums

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array bubble sort:", bubble_sort(arr))


#################################################################################
#################################################################################


# array divided into sorted at the beginning, unsorted at the end.
# inititially sorted is empty. repeatedly select smallest and 
# put at the end of sorted part.
# careful to track min_index instead of actual min for swap to work.
def selection_sort(nums):
    """
    TC, SC = O(n^2), O(1)
    best, worst = O(n^2), O(n^2)
    stable: No
    when to use:
        * when array is nearly sorted. 
        * small array when simplicity beneficial
        * memory constraint.
        * min data movement required since always makes at most n swaps.
    """
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array selection sort:", selection_sort(arr))


#################################################################################
#################################################################################


# Inserts each element into its correct position by comparing it with 
# elements to its left.
# outer loop on i runs from second element to last.
# key is outer loop element, inner while loop on j starts from
# index before key and searches if larger than key shift to right
# until it's not larger than key or end of beginning of array reached. 
# put key in while loop variable when exited.

# If array already sorted while loop exits immidiately, so only inner
# loop runs and complexity is O(n) 
def insertion_sort(arr):
    """
    TC, SC = O(n^2), O(1)
    best, worst = O(n^2), O(n^2)
    stable: Yes
    when to use:
        * when array is nearly sorted. 
        * small array when simplicity beneficial
        * memory constraint
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array insertion sort:", insertion_sort(arr))


#################################################################################
#################################################################################


def merge_sort(arr):
    """
    TC, SC = O(nlogn), O(n)
    best, worst = O(nlogn), O(nlogn)
    stable: Yes
    when to use:
        * large arrays
        * when stable sorting is requirement.
        * external sorting where data doesn't fit into memory.
    """
    if len(arr) <= 1:
        return arr
    merge_sort_helper(arr, 0, len(arr)-1)
    return arr

def merge_sort_helper(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort_helper(arr, left, mid)
        merge_sort_helper(arr, mid+1, right)

        i = left
        j = mid+1
        out = []
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:  # if equal pick from left to ensure stability.
                out.append(arr[i])
                i += 1
            else:
                out.append(arr[j])
                j += 1
        while i <= mid:
            out.append(arr[i])
            i += 1
        while j <= right:
            out.append(arr[j])
            j += 1

        # Copy the sorted subarray back into the original array
        # note arr[:] = out is wrong, need to update arr after left only
        for k in range(len(out)):
            arr[left + k] = out[k]

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array merge sort:", merge_sort(arr))


#################################################################################
#################################################################################


def merge_sort_simple(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(arr1, arr2):
    i, j = 0, 0
    out = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            out.append(arr1[i])
            i += 1
        else:
            out.append(arr2[j])
            j += 1
    out.extend(arr1[i:])
    out.extend(arr2[j:])
    return out

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array merge sort:", merge_sort_simple(arr))


#################################################################################
#################################################################################


# given two sorted list of integers, find if one is subset of other. 
def is_subset(s1, s2):
    i, j = 0, 0
    nums_matches = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            nums_matches += 1
        elif s1[i] < s2[j]:
            i += 1
        else:
            j += 1
    return nums_matches == min(len(s1), len(s2))


#################################################################################
#################################################################################


# external sort: Sort 256 billion 32-bit numbers with 16GB memory.
# what format is input data? text or binary? 
# binary more efficient in storage and I/O, text overhead of encode/decode.

# 256 billion * 4 bytes = 256 * 1G * 4 bytes = 1 TB
# allocate 1GB for os, 15 GB for sort. 
# 15 GB / 4 = 3.75 billion bytes to load in memory everytime.

input_file = "large_input.bin"
output_file = "sorted_output.bin"
chunk_size = 3_750_000_000 # same as 3750000000 for readability

def sort_large_file(input_file, output_file, chunk_size):
    chunk_files = []
    
    with open(input_file, 'rb') as f:
        chunk_num = 0
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            decimal_numbers = [int.from_bytes(data[i:i+4], byteorder='little') for i in range(0, len(data), 4)]
            decimal_numbers.sort() # efficient in-memory sort like quicksort or heapsort
            chunk_file = f'chunk_{chunk_num}.bin'
            with open(chunk_file, 'wb') as cf:
                for num in decimal_numbers:
                    cf.write(num.to_bytes(4, byteorder='little'))
            chunk_files.append(chunk_file)
            chunk_num += 1

    merge_chunks(chunk_files, output_file)

    for chunk_file in chunk_files:
        os.remove(chunk_file)


def merge_chunks(chunk_files, output_file):
    min_heap = []
    chunk_file_handles = [] # all chunk files need to be opened, keep track of file handles to close them later.

    for chunk_file in chunk_files:
        f = open(chunk_file, 'rb')
        chunk_file_handles.append(f)
        data = f.read(4)
        if data:
            number = int.from_bytes(data, byteorder='little')
            heapq.heappush(min_heap, (number, f))

    with open(output_file, 'rb') as out:
        while min_heap:
            smallest, f = min_heap.heappop()
            out.write(smallest.to_bytes(4, byteorder='little'))
            data = f.read(4)
            if data:
                number = int.from_bytes(data, byteorder='little')
                heapq.heappush(min_heap, (number, f))

    for f in chunk_file_handles:
        f.close()


#################################################################################
#################################################################################

# quick sort using Lomuto's partitioning 2 way.
# This can timout if many elements are equal to randomly selected pivot.
def quick_sort(nums):
    def helper(start, end):
        if start > end:
            return
        pind = random.randint(start, end)
        nums[pind], nums[start] = nums[start], nums[pind]
        orange = start
        for green in range(start+1, end+1):
            if nums[green] < nums[start]:
                orange += 1
                nums[orange], nums[green] = nums[green], nums[orange]
        nums[orange], nums[start] = nums[start], nums[orange]
        # orange is at pivot ind now and pivot is in final correct place.
        helper(start, orange-1)
        helper(orange+1, end)

    helper(0, len(nums)-1)
    return nums

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array quick sort:", quick_sort(arr))


#################################################################################
#################################################################################

# Quick sort using 3-way partitioning similar to Dutch National Flag problem,
# that also check if current element is equal to pivot. At the end 
# element smaller than pivot sit before low pointer and elements greater
# than pivot at after high pointer, and everything in between low and high (inclusive)
# is equal to pivot. We only recurse on left of low (<pivot) and right of high (>pivot).
def quick_sort_3way(nums):
    def helper(start, end):
        if start >= end:
            return
        
        # Three-way partitioning
        pivot_index = random.randint(start, end)
        pivot = nums[pivot_index]
        nums[pivot_index], nums[start] = nums[start], nums[pivot_index]
        
        low = start
        mid = start
        high = end

        while mid <= high:
            if nums[mid] < pivot:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] > pivot:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1

        # Recursive calls
        helper(start, low - 1)
        helper(high + 1, end)

    helper(0, len(nums) - 1)
    return nums

arr = [64, 34, 25, 12, 11, 22, 11, 90, 11]
print("Sorted array quick sort:", quick_sort_3way(arr))


#################################################################################
#################################################################################

# sort and array of 0's and 1's and 2's.
def dutch_national_flag(nums):
    low = 0
    curr = 0
    high = len(nums) - 1

    while curr <= high:
        if nums[curr] == 0:
            nums[low], nums[curr] = nums[curr], nums[low]
            low += 1
            curr += 1
        elif nums[curr] == 1:
            curr += 1
        else:  # nums[mid] == 2
            nums[high], nums[curr] = nums[curr], nums[high]
            high -= 1

    return nums

# Example usage
nums = [2, 0, 2, 2, 2, 0, 1, 1, 0]
print(dutch_national_flag(nums))


#################################################################################
#################################################################################

# Quick Select algorithm. LC 215
# timeout if we do two-way partitioning
def findKthLargest(nums, k):
    def helper(start, end, target_ind):
        if start >= end:
            return nums[start]
        
        pivot_index = random.randint(start, end)
        pivot = nums[pivot_index]
        nums[pivot_index], nums[start] = nums[start], nums[pivot_index]

        low = start
        mid = start
        high = end

        while mid <= high:
            if nums[mid] < pivot:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] > pivot:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1


        if target_ind >= low and target_ind <= high:
            return nums[target_ind]
        elif target_ind < low:
            return helper(start, low - 1, target_ind)
        else:
            return helper(high + 1, end, target_ind)

    return helper(0, len(nums) - 1, len(nums) - k)

nums = [3,2,3,1,2,4,5,5,6]
print(findKthLargest(nums, 4)) # output = 4
