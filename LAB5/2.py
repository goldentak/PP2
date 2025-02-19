import re

pattern = r'ab{2,3}'
test_strings = ["a", "ab", "abb", "ac", "b", "aBBB"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f'the element {string} mathes')
    else:
        print(f'the element {string} doesnt match')



