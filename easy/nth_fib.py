# write a function that gives the nth fib number (n-1) + (n-2)
# e.g. param n = 2 ->  return 1 (0, 1)
# e.g. param n = 6 ->  return 5 (0, 1, 1, 2, 3, 5)


# recursive O(2^n) time / O(1) space
def recursive_nth_fib(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    return recursive_nth_fib(n - 1) + recursive_nth_fib(n - 2)


# dynamic programing O(n) time / O(n) space
def dynamic_nth_fib(n):
    a = [0, 1]
    if n <= 1:
        return 0
    for i in range(2, n):
        result = a[i - 1] + a[i - 2]
        a.append(result)

    return a[-1]


# using dynamic programing with space optimization O(n) time / O(1) space
def dynamic_time_nth_fib(n):
    a = 0
    b = 1
    if n <= 1:
        return 0
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b


# tests

assert recursive_nth_fib(0) == 0
assert recursive_nth_fib(1) == 0
assert recursive_nth_fib(2) == 1
assert recursive_nth_fib(6) == 5
assert recursive_nth_fib(9) == 21

assert dynamic_nth_fib(0) == 0
assert dynamic_nth_fib(1) == 0
assert dynamic_nth_fib(2) == 1
assert dynamic_nth_fib(6) == 5
assert dynamic_nth_fib(9) == 21

assert dynamic_time_nth_fib(0) == 0
assert dynamic_time_nth_fib(1) == 0
assert dynamic_time_nth_fib(2) == 1
assert dynamic_time_nth_fib(6) == 5
assert dynamic_time_nth_fib(9) == 21
