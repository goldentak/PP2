#lists
mylist = ["apple", "banana", "cherry", "cherry"] #Shortly, how to declare a list
print(mylist)
print(len(mylist)) # we can find length of list by this method len()

list1 = ["abc", 34, True, 40, "male"] #unlike arrays, lists may contain elements of various data types in the same time 
print(type(mylist))  #So the output is <class 'list'>, it is not an array

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
#alternative method to open a list

#we can access to the elemnts of list by index:
mylist[1] #returns second element, because index starts from zero
print(thislist[-1]) #it also can be negative
print(thislist[2:4]) #printing the elements in range
print(thislist[:4]) #means from the first to 4 (last is not including)

thislist[1] = "blackcurrant" #easily changing an existing element
thislist[1:3] = ["blackcurrant", "watermelon"] #Now with slicing
thislist.insert(2, "watermelon") # alternative method

thislist.append("orange") # adding a new element to the list
tropical = ["mango", "pineapple", "papaya", "banana"]
thislist.extend(tropical) #Allows extending the list with another one

thislist.remove("banana") #removes by element
thislist.pop(1) #removes by index (if argument is null, deletes last one)
del thislist[0]
thislist.clear() #removes all elements from the list

thislist = list(("apple", "banana", "cherry"))
#loops 
for x in thislist:
  print(x)
#or
for i in range(len(thislist)):
  print(thislist[i])
#or
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#and
[print(x) for x in thislist]
#these methods bases on different things, but output will be same

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
#syntax:: [expression for item in iterable if condition == True]
thislist.sort(reverse = True)

# def myfunc(n):
#   return abs(n - 50)
# thislist.sort(key = myfunc) #You can also customize your own function by using the keyword argument
thislist.sort(key = str.lower) #it's built-in key function that filters sorting by lower and upper signs

mylist = thislist.copy() #copy
mylist = thislist[:] #or like that

#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 #joining two lists to the general one
list1.extend(list2) # or like this, result is the same 

list.append(x)    # Adds x to the end of the list
list.clear()      # Removes all elements from the list
list.copy()       # Returns a shallow copy of the list
list.count(x)     # Counts occurrences of x in the list
list.extend(iter) # Extends the list by appending elements from iter
list.index(x)     # Returns the index of the first occurrence of x
list.insert(i, x) # Inserts x at index i
list.pop(i)       # Removes and returns the item at index i (default last)
list.remove(x)    # Removes the first occurrence of x
list.reverse()    # Reverses the elements of the list in place
list.sort()       # Sorts the list in ascending order

