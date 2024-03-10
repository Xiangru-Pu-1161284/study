import random

def check_sorted(nums):
    if len(nums) < 2:
        return True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True
    
def bogosort(nums):
    #your code here
    while not check_sorted(nums):
        random.shuffle(nums)
        print(nums)
    return nums

list = [2,4,1,5,2]
print(bogosort(list))