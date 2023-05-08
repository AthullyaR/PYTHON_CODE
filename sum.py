#Given an array of integers num and an integer n, return indices of the two numbers such that they add up to n."
def sum(num,n):
    f,r=0,len(num)-1
    while f<r:
        if num[f]+num[r]>n:
            r-=1
        elif num[f]+num[r]<n:
            f+=1
        else:
            print(f+1,r+1)
            return[f+1,r+1]
     
l=[2,3,4,7,8]
n=7     
a=sum(l,n)      
print(a)
      

  