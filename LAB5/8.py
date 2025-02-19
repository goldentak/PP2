import re


test_strings = [
    "helloWorld",
    "Hello",
    "test_case",
    "another_example",
    "JustText",
    "snake_case_example",
    "UpperCamelCase",
    "kebab-case-example",
    "123_numbers_only",
    "email@example.com",
    "example@domain.co.uk",
    "+999 (999) 1231-45-67",
    "42",
    "no_numbers_here",
    "UPPERCASE",
    "mixedUP_and_down",
    "___underscores___",
    "     spaces around    ",
    "special#chars!@&*()",
    "",
    "a",
    "a_b",
    "a__b",
    "abc_def_ghi",
    "hello_my_dears",
    "kebab",
    "bek"
]
for string in test_strings:
    if re.search(r'[A-Z][^A-Z]*', string):
        result = re.findall(r'[A-Z][^A-Z]*', string)
        print(' '.join(result))
