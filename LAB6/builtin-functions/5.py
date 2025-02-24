def isTupTrue(tup):
    return all(tup)

tup1 = (True, True, True)
tup2 = (False, False, True)

print(isTupTrue(tup1))
print(isTupTrue(tup2))