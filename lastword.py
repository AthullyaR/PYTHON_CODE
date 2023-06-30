"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
"""
"""
def last(s):
    for x in s:
        count=0
        print(x)
        count=count+len(x)
        
    return count
    """
"""
def last(s):
    count=0
    for x in s:
        if x==" ":
            count=0
        else:
            count+=1
        
    return count
"""



s=input("enter:")
print(len(s.split()[-1]))