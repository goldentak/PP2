import re

def camel_to_snake(s):
    snake = re.sub(r'(?<!^)(?=[A-Z])', '_', s)
    return snake.lower()


strings = [
    "CamelCase",
    "camelCaseExample",
    "HTTPRequest",
    "SimpleTest",
    "justCamel"
]

for s in strings:
    print(f"result:: {camel_to_snake(s)}")
