def removeelements(nums,val):
    o=[]
    for x in nums:
        if x!=val:
            o.append(x)
    nums=o
    print(nums)
    return len(o)
nums=list(map(int,input().split()))
val=int(input("val:"))
f=removeelements(nums,val)
print(f)