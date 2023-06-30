c=0
    b=False
    i=0
    while i>=0 :

        c+=nums[i]
        i+=nums[i]

        if c==(len(nums)-1):
            b=True
            return b

        if nums[i]==0:
            break
        
        
    return b