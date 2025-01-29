# 11  | Write a Python function that checks whether a word or phrase is palindrome

def isPolindrom(s):
    revs = s[::-1]
    if revs == s:
        print(True)
        return True
    print(False)
    return False

isPolindrom("Hello")
isPolindrom("kazak")
