#Operators
x = 1 
y = 2

x + y  # Addition
x - y  # Subtraction
x * y  # Multiplication
x / y  # Division
x % y  # Modulus
x ** y  # Exponentiation
x // y  # Floor division


x = 5      # Assignment
x += 3     # x = x + 3
x -= 3     # x = x - 3
x *= 3     # x = x * 3
x /= 3     # x = x / 3
x %= 3     # x = x % 3
x //= 3    # x = x // 3
x **= 3    # x = x ** 3
x &= 3     # x = x & 3
x |= 3     # x = x | 3
x ^= 3     # x = x ^ 3
x >>= 3    # x = x >> 3
x <<= 3    # x = x << 3
print(x := 3)  # x = 3, then print(x)

#Comparison Operators 
# How it defines: == (equal to), != (Not equal), > (Greater than), < (Less than), >= / <= (Greater/ less than or equal to)

#logical operations
# and (returns True if both True, otherwise False)
# or (returns True if exists at least 1 True, otherwise False)
# not (inverse operator)

#Identity Operations 
x is y      # Returns True if x and y are the same object
x is not y  # Returns True if x and y are not the same object

#Membership Operators
x in y      # Returns True if x is present in y
x not in y  # Returns True if x is not present in y

#Bitwise Operators
x & y   # AND: Sets each bit to 1 if both bits are 1
x | y   # OR: Sets each bit to 1 if at least one bit is 1
x ^ y   # XOR: Sets each bit to 1 if only one of the bits is 1
~x      # NOT: Inverts all the bits
x << 2  # Left shift: Shifts bits of x left by 2 positions, filling with zeros
x >> 2  # Right shift: Shifts bits of x right by 2 positions, filling with leftmost bit (sign-extended)
