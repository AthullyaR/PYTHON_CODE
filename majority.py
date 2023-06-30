"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

"""
def majority(nums):
    major=0
    n=len(nums)
    for x in nums:
        if nums.count(x)>(n/2):
            major=x
    return major
"""

"""
from collections import Counter

def majority(nums):
    # Size of the given array
    n = len(nums)

    # Count the occurrences of each element using Counter
    counter = Counter(nums)
    print(counter.items())

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1
    """
"""
Optimal Approach: Moore’s Voting Algorithm
"""

def majority(nums):
    count=0
    element=None
    for x in nums:
        if count==0:
            count=1
            element=x
        elif x==element:
            count+=1
        else:
            count-=1

    return element

nums=list(map(int, input().split()))
print(majority(nums))
