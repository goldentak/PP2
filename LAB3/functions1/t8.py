# 8  | Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    zeroCnt = 0
    for i in nums:
        if i == 0:
            zeroCnt += 1
        elif zeroCnt >= 2 and i == 7:
            return True
        
    return False

spyGame = [1,2,4,7 ,0,0,5]
print(spy_game(spyGame))