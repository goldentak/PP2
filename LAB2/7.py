#if else, Conditions and If statements
a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif instead of else if
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b")
print("A") if a > b else print("B") #short versions 
print("A") if a > b else print("=") if a == b else print("B")

if b > a:
  pass #to avoid getting an error