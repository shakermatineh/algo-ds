
# outer loop on all elements i
# inner loop j reversed from last element to one right after i
# at the end of each inner loop, smallest element bubbles down at its final place.
# best case is O(n) when array sorted, use a flag to exit early. 
def bubble_sort(nums):
	"""
	TC, SC = O(n^2), O(1)
	best, worst = O(n), O(n^2)
	stable: Yes
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


# outer loop on i runs from second element to last.
# key is outer loop element, inner while loop on j starts from
# index before key and searches if larger than key shift to right
# until it's not larger than key or end of beginning of array reached. 
# put key in while loop variable when exited.

# If array already sorted while loop exits immidiately, so only inner
# loop runs and complexity is O(n) 

# At the end of each inner loop key is placed at its correct
# position within sorted portion or array.
def insertion_sort(arr):
	"""
	TC, SC = O(n^2), O(1)
	best, worst = O(n^2), O(n^2)
	stable: No
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
print("Sorted array:", insertion_sort(arr))
