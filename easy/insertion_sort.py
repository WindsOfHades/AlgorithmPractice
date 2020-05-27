"""
write an insertion sort
"""


# time best: O(n) only if we are lucky and the array was already sorted!
# time worst: O(n^2)
# space O(1)
def insertion_sort_2(array):
    position = 1
    while position < len(array):
        marker = position
        for i in range(position - 1, -1, -1):
            if array[i] > array[marker]:
                swap(array, i, marker)
                marker -= 1

        position += 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# same solution as above in a cleaner way
def insertion_sort(array):
    for i in range(1, len(array)):
        marker = i
        while marker > 0 and array[marker] < array[marker - 1]:
            swap(array, marker, marker - 1)
            marker -= 1
    return array


# tests
def test_empty():
    a = []
    assert insertion_sort(a) == a


def test_one_element():
    a = [1]
    assert insertion_sort(a) == a


def test_normal():
    a = [7, 9, -1, 0, 14, 2]
    assert insertion_sort(a) == [-1, 0, 2, 7, 9, 14]


def test_normal_2():
    a = [8, 5, 2, 9, 5, 6, 3]
    assert insertion_sort(a) == [2, 3, 5, 5, 6, 8, 9]


def test_reverse():
    a = [5, 4, 3, 2, 1, 0, -1]
    assert insertion_sort(a) == [-1, 0, 1, 2, 3, 4, 5]
