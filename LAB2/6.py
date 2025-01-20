#dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"] #items can be of any data type
}
print(thisdict)
print(thisdict["brand"]) #out:: "Ford"
#Python version 3.7+, dictionaries are ordered
print(len(thisdict)) #out:: 3
print(type(thisdict))  #<class 'dict'>

thisdict2 = dict(name = "John", age = 36, country = "Norway") #alternative way to create a dict

#Access
x = thisdict["model"] #or>
x = thisdict.get("model")
x = thisdict.keys() #to get all keys from the tuple
y = thisdict.values() #to get all values
z = thisdict.items() #to get "key-value" items
thisdict2["name"] = "Walter White" #dictionaries are changeable 

#check for a key
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict.update({"year": 2020}) #to update data

#removing data
thisdict.pop("model") #by name of element
thisdict.popitem() #by its index
del thisdict["model"]
del thisdict # to delete dict
thisdict.clear() #to delete all data from dict

#loops
for x in thisdict:
  print(x)

mydict = dict(thisdict) #to copy

#nested dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

dict.clear()                        # Removes all elements from the dictionary
dict.copy()                         # Returns a shallow copy of the dictionary
dict.fromkeys(seq, value)           # Creates a dictionary with keys from seq and values set to value
dict.get(key, default=None)         # Returns the value of the specified key, or default if key is not found
dict.items()                        # Returns a view object with key-value pairs as tuples
dict.keys()                         # Returns a view object with the dictionary's keys
dict.pop(key, default=None)         # Removes the specified key and returns the value, or default if key is not found
dict.popitem()                      # Removes and returns the last inserted key-value pair
dict.setdefault(key, default=None)  # Returns the value of key; inserts key with default if not present
dict.update(other)                  # Updates the dictionary with key-value pairs from other, overwriting existing keys
dict.values()                       # Returns a view object with the dictionary's values
