"""
Remove duplicates from array
"""

"""
def removeduplicates(nums):
    o=[]

    for x in nums:
        if x in o:
            continue
        else:
            o.append(x)
    
    nums=o
    print(nums)
    return (len(nums))
    """




def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    print(nums)
    return i + 1

nums=list(map(int,input().split()))
f=removeDuplicates(nums)
print(f)