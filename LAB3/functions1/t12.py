# 12  | Define a functino histogram() that takes a list of integers and prints a histogram to the screen

def histogram(length):
    for i in length:
        print('*' * i)

histogram([4, 9, 7])