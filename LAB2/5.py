#Sets
myset = {"apple", "banana", "cherry"} #declaring set
print(myset)

#sets can hold elements with different data types
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(len(thisset)) #len
print(type(myset)) #<class 'set'>

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
#alternative method of declaring

#access
for x in thisset:
  print(x) #by the loop

print("banana" in thisset) #returns True
print("banana" not in thisset) #returns False

thisset.add("orange") #Analogue of append method for lists


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical) #combines both sets into the first one
print(thisset) 

#removing items
thisset.remove("banana") #by element
thisset.discard("apple") #or like that
x = thisset.pop() #by index
thisset.clear() #removes all elements
del thisset #deletes this set completely

thisset = {"apple", "banana", "cherry"}

#join
#The union() and update() methods joins all items from both sets.
#The intersection() method keeps ONLY the duplicates.
#The difference() method keeps the items from the first set that are not in the other set(s).
#The symmetric_difference() method keeps all items EXCEPT the duplicates.

a = {1, 2, 3, 4, 5}
b = {2, 4, 6, 8, 10}
print(a.add(b))                            # Adds element b to set a
print(a.clear())                           # Removes all elements from set a
print(a.copy())                            # Returns a copy of set a
print(a.difference(b))                     # Returns a set with elements in a but not in b
print(a.difference_update(b))              # Removes elements in b from set a
print(a.discard(b))                        # Removes element b from set a if it exists
print(a.intersection(b))                   # Returns a set with elements common to a and b
print(a.intersection_update(b))            # Keeps only elements in both a and b
print(a.isdisjoint(b))                     # Returns True if a and b have no elements in common
print(a.issubset(b))                       # Returns True if all elements of a are in b
print(a < b)                               # Checks if a is a proper subset of b
print(a.issuperset(b))                     # Returns True if all elements of b are in a
print(a > b)                               # Checks if a is a proper superset of b
print(a.pop())                             # Removes and returns an arbitrary element from a
print(a.remove(b))                         # Removes element b from a, raises KeyError if b is not in a
print(a.symmetric_difference(b))           # Returns a set with elements in either a or b but not both
print(a.symmetric_difference_update(b))    # Updates a with elements in either a or b but not both
print(a.union(b))                          # Returns a set with all elements from a and b
print(a.update(b))                         # Adds elements from b to a
