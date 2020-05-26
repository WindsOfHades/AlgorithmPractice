"""
write a function that takes in an array and returns the three largest numbers inside without sorting the input array

Notes:
    - the result should be sorted
    - duplicates are ok to have

example:
[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
[18, 141, 541]
"""


# O(n) time O(1) space
def three_largest(array):
    storage = []
    counter = 0

    for i in array:
        if counter > 2:
            minimum = min(storage)
            if i > minimum:
                minimum_index = storage.index(minimum)
                storage[minimum_index] = i
        else:
            storage.append(i)
        counter += 1
    return sorted(storage)


# tests
def test_empty():
    a = []
    assert three_largest(a) == []


def test_on_element():
    a = [2]
    assert three_largest(a) == a


def test_three_elements():
    a = [3, 2, -1]
    assert three_largest(a) == [-1, 2, 3]


def test_mix():
    a = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    assert three_largest(a) == [18, 141, 541]
