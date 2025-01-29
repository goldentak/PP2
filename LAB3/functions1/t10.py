# 10  | Write a Python function that takes a list and returns a new list with unique elements of the first list

def makeUnique(arr):
    arr.sort()
    newArr = []
    for i in arr:
        if i not in newArr:
            newArr.append(i)
    print(*newArr)
    return newArr

makeUnique([1, 4, 5, 2, 5, 3, 1, 5, 8, 5, 3, 4, 5, 1, 7])