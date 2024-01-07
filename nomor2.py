# soal nomor 2.1
def prim(x):
    return x

result = prim(13)
print(result)


# soal nomor 2.2
def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()

    def is_palindrome_recursive(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])

    return is_palindrome_recursive(cleaned_string)

input_str = "kasur rusak"
result = is_palindrome(input_str)
print(result)
