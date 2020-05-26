"""
implement binary search

Notes:
    - input array is sorted
    - return -1 if not found otherwise the index of found
"""


# O(log(n)) time O(1) space
def binary_search(array, target):
    start = 0
    finish = len(array) - 1

    while start <= finish:
        middle = (finish + start) // 2
        potential = array[middle]
        if potential == target:
            return middle
        elif potential > target:
            finish = middle - 1
        else:
            start = middle + 1

    return -1


def test_empty():
    a = []
    assert binary_search(a, 1) == -1


def test_one_element_find():
    a = [1]
    assert binary_search(a, 1) == 0


def test_one_element_not_find():
    a = [1]
    assert binary_search(a, 0) == -1


def test_two_elements():
    a = [1, 2]
    assert binary_search(a, 2) == 1


def test_last_element_target_even():
    a = [1, 2, 3, 4]
    assert binary_search(a, 4) == 3


def test_last_element_target_odd():
    a = [1, 2, 3, 4, 5]
    assert binary_search(a, 5) == 4


def test_normal():
    a = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    assert binary_search(a, 33) == 3


# test_two_elements()
