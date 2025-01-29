# 7  | Given a list of ints, return True if the array contains a 3 next to a 3 somewhere

def has_33(nums = []):
    for i in range(1, len(nums) - 1):
        if nums[i - 1] == 3 and nums[i] == nums[i - 1]:
            return True
        
    return False


nums = [1, 3, 3, 4]
print(has_33(nums))