"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

"""
def rotate(nums,k):
    k %= len(nums)

            new_num = nums[-k:]+nums[:-k]
            # print(new_num)
            for i in range(len(nums)):
                nums[i] = new_num[i]
"""

def rotate(nums,k):
    """
    for i in range(k):
        
        nums.insert(0,nums[-1])
        nums=nums[:-1]
    """
    x=k%len(nums)
    def rev(s,e):
        while(s<e):
            nums[s],nums[e]=nums[e],nums[s]
            s+=1
            e-=1
    
    nums.reverse()
    print(nums)
    rev(0,x-1)
    print(nums)
    rev(x,len(nums)-1)
    print(nums)

nums=list(map(int,input().split()))


k=int(input("enter k:"))
rotate(nums,k)
"""
identify the reverse and revsersed
"""