"""
def reverse(s):
    st=" "
    for i in range(len(s)-1,-1,-1):
            st+=(s[i])
            st+=" "
    return st
"""
def reverse(s):
    return ' '.join(reversed(s.split()))
n=input("enter:").split()
print(reverse(n))