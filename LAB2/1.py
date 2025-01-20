#booleans
print(10 > 9) #True
print(10 == 9) #True
print(10 < 9) #False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #we can make simple conditions with that

print(bool("Hello")) #True
print(bool(15)) #True
bool(["apple", "cherry", "banana"]) #also True because of they have at least some content in themselfes


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) # all the examples from this block is False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
# Returns False cause of the len of object (we didnt cover this topic yet)

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int)) #isinstance determines object's data type
