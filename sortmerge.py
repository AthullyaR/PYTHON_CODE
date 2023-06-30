"""
Merge Sorted Array
"""

def sortmerge(num1,num2,m,n):
    i=0
    for x in range(m):
        if i>=n:
            break
        
        if num1[x]==0:
            num1[x]=num2[i]
            i=i+1
            
    num1.sort()
    return num1

num1=list(map(int,input().split()))

m=len(num1)
num2=list(map(int,input().split()))

n=len(num2)
f=sortmerge(num1,num2,m,n)
print(f)