"""
Remove duplicates with each element atmost occurs twice
"""

def remove(nums):
    for num in nums:
            while nums.count(num) > 2:
                nums.remove(num)
         
    print(nums)

    return len(nums)

nums=list(map(int,input().split()))
f=remove(nums)
print(f)