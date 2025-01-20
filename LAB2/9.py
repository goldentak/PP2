#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
for x in range(6):
  print(x)

for x in range(2, 6): #2, 3, 4, 5
  print(x)
 
for x in range(2, 30, 3): #third value is step
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) #nested loops

for x in [0, 1, 2]:
  pass