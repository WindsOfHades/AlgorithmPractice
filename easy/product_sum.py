"""
Write a function that takes in a special array (can contain other special arrays) and return the product sum of elements

note if there are other special arrays inside the sum of its elements are multiplied by their level.

e.g.

12 <---  5+2 + 2*(7 - 1) + 3 + 2*(6 + 3*(-13 + 8) + 4) <--- [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


"""


# O(n) time O(r) space [r is the number of recursive call stacks]
def product_sum(array, multiplier=1):
    sum = 0
    for i in array:
        if isinstance(i, list):
            multiplier += 1
            sum += product_sum(i, multiplier=multiplier)
            multiplier -= 1
        else:
            sum += i
    return sum * multiplier


# tests (run with pytest)
def test_flat():
    a = [1, 2, 3]
    assert product_sum(a) == 6


def test_empty():
    a = []
    assert product_sum(a) == 0


def test_nested_empty():
    a = [[]]
    assert product_sum(a) == 0


def test_nested_2():
    a = [1, [1, [1, -1]]]
    assert product_sum(a) == 3


def test_nested_3():
    a = [1, [1, [1, -1], 1]]
    assert product_sum(a) == 5


def test_nested_4():
    a = [3, [6, [-13, 8], 4]]
    assert product_sum(a) == -7


def test_nested_5():
    a = [[6, [-13, 8], 4]]
    assert product_sum(a) == -10


def test_nested_6():
    a = [5, 2, 3, [6, [-13, 8], 4]]
    assert product_sum(a) == 0


def test_nested():
    a = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    assert product_sum(a) == 12
