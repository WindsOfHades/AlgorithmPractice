"""
write a selection sort
"""


# time best: O(n^2)
# time worst: O(n^2)
# space O(1)
def selection_sort(array):
    smallest_position = 0
    for i in range(len(array)):
        smallest_position = i
        for j in range(i, len(array)):
            if array[smallest_position] > array[j]:
                smallest_position = j
        swap(array, smallest_position, i)

    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


################## tests ##################


def test_empty():
    a = []
    assert selection_sort(a) == a


def test_one_element():
    a = [1]
    assert selection_sort(a) == a


def test_normal():
    a = [7, 9, -1, 0, 14, 2]
    assert selection_sort(a) == [-1, 0, 2, 7, 9, 14]


def test_normal_2():
    a = [8, 5, 2, 9, 5, 6, 3]
    assert selection_sort(a) == [2, 3, 5, 5, 6, 8, 9]


def test_reverse():
    a = [5, 4, 3, 2, 1, 0, -1]
    assert selection_sort(a) == [-1, 0, 1, 2, 3, 4, 5]
