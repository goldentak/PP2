def is_palindrome(s):
    s = s.replace(" ", "").lower()
    rev = ""
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]
    return s == rev

s = "level"
print(f'"{s}" is a palindrome.' if is_palindrome(s) else f'"{s}" is not a palindrome.')
