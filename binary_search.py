import bisect
def find_rightmost_insert(nums, target):
    # Start binary search with left = 0 and right = len(nums) - 1
    left, right = 0, len(nums) - 1

    # If nums is empty, return 0 for the insertion position
    if len(nums) == 0:
        return 0, 0
    
    # Binary search for rightmost insert position
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1  # Move right if target is greater or equal to nums[mid]
        else:
            right = mid - 1  # Move left if target is smaller

    # At the end of this loop, left will be the insert position after the last occurrence of target
    # If target is in nums, nums[left-1] should be target (if left > 0)

    # Validate by comparing with bisect_right result
    ind = bisect.bisect_right(nums, target)

    return left, ind


def find_rightmost_insert_old(nums, target):
	# this is confusing.
	# find the rightmost insert position
	left, right = 0, len(nums) # this is for len=0, otherwise not entering the loop.
	while left < right:
		mid = left + (right - left) // 2
		if nums[mid] <= target:
			left = mid + 1
		else:
			right = mid
	# now left and right point to the insert position
	# exactly after last target, if exists
	# nums[left-1] = target

	# another way:
	ind = bisect.bisect_right(nums, target)
	return left, ind



print("AAAAAAA")
print(find_rightmost_insert([2,4,5,7,9,9,9,10,12], 9))
print(find_rightmost_insert([5,7,9,9,9,10,12,13,14], 9))
print(find_rightmost_insert([9,9], 9))
print(find_rightmost_insert([9], 9))
print(find_rightmost_insert([11], 9))
print(find_rightmost_insert([5], 9))
print(find_rightmost_insert([1,2,3,4], 9))

print("BBBBBBB")
print(find_rightmost_insert_old([2,4,5,7,9,9,9,10,12], 9))
print(find_rightmost_insert_old([5,7,9,9,9,10,12,13,14], 9))
print(find_rightmost_insert_old([9,9], 9))
print(find_rightmost_insert_old([9], 9))
print(find_rightmost_insert_old([11], 9))
print(find_rightmost_insert_old([5], 9))
print(find_rightmost_insert_old([1,2,3,4], 9))


def find_leftmost_insert(nums, target):
    # Start binary search with left = 0 and right = len(nums) - 1
    left, right = 0, len(nums) - 1

    # If nums is empty, return 0 for the insertion position
    if len(nums) == 0:
        return 0, 0
    
    # Binary search for leftmost insert position
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid - 1  # Move left to find smaller index
        else:
            left = mid + 1  # Move right if target is greater than mid
    
    # At the end of this loop, left will be the leftmost insertion point
    # or the position of the first occurrence of the target.

    # Validate by comparing with bisect_left result
    import bisect
    ind = bisect.bisect_left(nums, target)

    return left, ind  # Return both your calculated index and bisect's index




def insert_sorted(nums, target):
	bisect.insort(nums, target)
	return nums
print(insert_sorted([2,4,5,7,9,9,9,10,12], 9))


def find_leftmost_insert_old(nums, target):
	left, right = 0, len(nums)
	while left < right:
		mid = left + (right - left) // 2
		if nums[mid] >= target:
			right = mid
		else:
			left = mid + 1
	# now left and right point to insert position or
	# leftmost element equal to target, if exists.
	# nums[left] = target
	ind = bisect.bisect_left(nums, target)
	return left, ind

print("CCCCCCC")
print(find_leftmost_insert([2,4,5,7,9,9,9,10,12], 9))
print(find_leftmost_insert([5,7,9,9,9,10,12,13,14], 9))
print(find_leftmost_insert([9,9], 9))
print(find_leftmost_insert([9], 9))
print(find_leftmost_insert([11], 9))
print(find_leftmost_insert([5], 9))
print(find_leftmost_insert([1,2,3,4], 9))
