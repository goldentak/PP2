# 5  |  Write a function that accepts string from user and print all permutations of that string.

def next_permutation(s):
    if len(s)==1:
        return [s]
    new1=[]
    for i in range(len(s)):
        for x in next_permutation(s[:i]+s[i+1:]):
            new1.append(s[i]+x)
    return new1
print(next_permutation("ggg"))