"""
Caesar cipher encryptor is a function that gets a string along with a key (number).

The encryption original string  characters will be pushed +key chars in the alphabet

"""


# O(n) time O(n) space
def cesar_cipher(original_string, key):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    result = ""

    for char in original_string:
        try:
            index = alphabet.index(char) + key
            if index >= len(alphabet) - 1:
                index = index % len(alphabet)
            char = alphabet[index]
        except ValueError:
            pass
        result += char
    return result


a = "xyz"
b = 2
result = cesar_cipher(a, b)
assert result == "zab"

a = "x y z"
b = 26
result = cesar_cipher(a, b)
assert result == "x y z"

a = "x y z"
b = 28
result = cesar_cipher(a, b)
assert result == "z a b"

a = ""
b = 2
result = cesar_cipher(a, b)
assert result == ""

a = "12a3"
b = 5
result = cesar_cipher(a, b)
assert result == "12f3"
