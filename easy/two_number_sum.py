# write a function that gets a non empty array and a target sum
# if there are any 2 numbers in the array that sump up to given target
# return them in an array else empty array should be returned

# * the two numbers should be different
# * assume there is only one or no pairs as a result


# O(n^2) bruteforce approach
def sum_two_numbers_naive(arr, target):
    for i in arr:
        for j in arr:
            if i != j and i + j == target:
                return sorted([i, j])
    return []


# O(n) time O(n) space
def sum_two_numbers(arr, target):
    desired_num_map = {}
    for num in arr:
        desired_num = target - num
        if desired_num != num and desired_num in desired_num_map:
            return sorted([num, desired_num])
        else:
            desired_num_map[num] = True
    return []


# O(nlogn) time O(1) space
def sum_two_numbers_nlogn(arr, target):
    arr.sort()  # O(nlogn)
    left = 0
    right = len(arr) - 1
    while left < right:  # O(n)
        current_sum = arr[left] + arr[right]
        if (current_sum == target):
            if (arr[left] != arr[right]):
                return [arr[left], arr[right]]
            else:
                left += 1
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
    return []


# tests
assert sum_two_numbers_naive([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
assert sum_two_numbers_naive([3, 5, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
assert sum_two_numbers_naive([], 10) == []
assert sum_two_numbers_naive([1, 2], 10) == []
assert sum_two_numbers([1, 1], 2) == []

assert sum_two_numbers([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
assert sum_two_numbers([3, 5, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
assert sum_two_numbers([], 10) == []
assert sum_two_numbers([1, 2], 10) == []
assert sum_two_numbers([1, 1], 2) == []

assert sum_two_numbers_nlogn([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
assert sum_two_numbers_nlogn([3, 5, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
assert sum_two_numbers_nlogn([], 10) == []
assert sum_two_numbers_nlogn([1, 2], 10) == []
assert sum_two_numbers_nlogn([1, 1], 2) == []
