"""
Write a function that takes a string and checks if it is palindrome
palindrome string is a string that is written the same in backwards.

example : abba

Notes:
single char string is palindrome as well

"""


# O(n) time O(1) space (best way I think)
def is_palindrome_with_pointers(input_string):
    start = 0
    end = len(input_string) - 1
    while start <= end:
        if input_string[start] == input_string[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


# O(n) time O(n) space
def is_palindrome_with_string_reverse(input_string):
    reverse = input_string[::-1]
    return reverse == input_string


# tests

a = "abba"
result = is_palindrome_with_pointers(a)
assert result is True

a = "abbz"
result = is_palindrome_with_pointers(a)
assert result is False

a = "a"
result = is_palindrome_with_pointers(a)
assert result is True

a = "abcdcba"
result = is_palindrome_with_pointers(a)
assert result is True

a = ""
result = is_palindrome_with_pointers(a)
assert result is True

# ----

a = "abba"
result = is_palindrome_with_string_reverse(a)
assert result is True

a = "abbz"
result = is_palindrome_with_string_reverse(a)
assert result is False

a = "a"
result = is_palindrome_with_string_reverse(a)
assert result is True

a = "abcdcba"
result = is_palindrome_with_string_reverse(a)
assert result is True

a = ""
result = is_palindrome_with_string_reverse(a)
assert result is True
