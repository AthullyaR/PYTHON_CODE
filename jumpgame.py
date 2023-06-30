"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""
def jump(nums):
    maximum =0

    for i in range(len(nums)):

        if i > maximum:

            return False

        maximum = max(maximum,i+nums[i])
        print(i,maximum)

    return True

nums=list(map(int,input().split()))
print(jump(nums))