#Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))


#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1)) #<class 'tuple'>

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #Alternative method to declare a tuple

#You can access tuple items by referring to the index number, inside square bracke
print(thistuple[1])


#Once a tuple is created, you cannot change its values
#they do not have a built-in append() method
#but we can delete it
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists
 
#unpacking tuple (with Asterisk)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


thistuple = ("apple", "banana", "cherry")
#as the other exmples, we also can iterate tuple by for loop
for x in thistuple:
  print(x)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
#joining tuples
tuple3 = tuple1 + tuple2

tuple1.count("a")  # Returns the number of times x appears in the tuple
tuple2.index(1)  # Returns the index of the first occurrence of x in the tuple


