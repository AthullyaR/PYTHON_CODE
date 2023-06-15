def merge(word1,word2):
    len1=len(word1)
    len2=len(word2)
    r=0
    result=[]
    for i, j in zip(word1,word2):
        result.append(i)
        result.append(j)
        r=r+1

    if i!=len1:
        result.append(word1[r:])

    if i!=len1:
        result.append(word2[r:])

    stringans=""
    return (stringans.join(result))


a=input("enter:")
b=input("enter:")
f=merge(a,b)
print(f)

