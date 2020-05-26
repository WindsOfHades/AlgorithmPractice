"""
write a bubble sort
"""


# time best: O(n) only if we are lucky and the array was already sorted!
# time worst: O(n^2)
# space O(1)
def bubble_sort(array):
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                is_sorted = False
        counter += 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# tests
def test_empty():
    a = []
    assert bubble_sort(a) == a


def test_one_element():
    a = [1]
    assert bubble_sort(a) == a


def test_normal():
    a = [7, 9, -1, 0, 14, 2]
    assert bubble_sort(a) == [-1, 0, 2, 7, 9, 14]


def test_reverse():
    a = [5, 4, 3, 2, 1, 0, -1]
    assert bubble_sort(a) == [-1, 0, 1, 2, 3, 4, 5]


test_normal()