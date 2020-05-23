"""

write a function that gets 2 arrays and returns true if the second array items appear in the same order
inside the first array.

example:
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

notes:
a signle number or the whole array are subsequence of the original array

"""


# O(n) time O(1) space
def is_valid_subsequence(array, sequence):
    array_pointer = 0
    sequence_pointer = 0
    if not sequence:
        return True
    if len(sequence) > len(array):
        return False
    while array_pointer < len(array):
        if sequence[sequence_pointer] == array[array_pointer]:
            sequence_pointer += 1
        array_pointer += 1
        if sequence_pointer == len(sequence):
            return True
    return False


# tests
a = [5, 1, 22, 25, 6, -1, 8, 10]
b = [1, 6, -1, 10]
assert is_valid_subsequence(a, b) is True

a = [5, 1, 22, 25, 6, -1, 8, 10]
b = [5, 1, 22, 25, 6, -1, 8, 10]
assert is_valid_subsequence(a, b) is True

a = [5, 1, 22, 25, 6, -1, 8, 10]
b = []
assert is_valid_subsequence(a, b) is True

a = [5, 1, 22, 25, 6, -1, 8, 10]
b = [22]
assert is_valid_subsequence(a, b) is True

a = [5, 1, 22, 25, 6, -1, 8, 10]
b = [22, 1]
assert is_valid_subsequence(a, b) is False

a = [5, 1, 22, 25, 6, -1, 8, 10]
b = [5, 1, 22, 22, 25, 6, -1, 8, 10]
assert is_valid_subsequence(a, b) is False

a = [1, 1, 6, 1]
b = [1, 1, 1, 6]
assert is_valid_subsequence(a, b) is False

a = [5, 1, 22, 25, 6, -1, 8, 10]
b = [1, 6, -1, 10, 11, 11, 11, 11]
assert is_valid_subsequence(a, b) is False
