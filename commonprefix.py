def common(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:len(prefix) - 1]
            if not prefix:
                return ""
    
    return prefix

n=input("enter:").split()
print(common(n))