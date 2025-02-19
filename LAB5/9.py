import re

def insert_spaces(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

# Примеры
strings = [
    "HelloWorld",
    "UpperCamelCase",
    "simpleTest",
    "mixedUP_and_down",
    "JustText",
    "UPPERCASE",
    "hello"
]

for s in strings:
    print(f"result:: {insert_spaces(s)}")
