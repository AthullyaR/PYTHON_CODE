"""
def roman(num):
    val=0
    d={ 'I'  :  1,
        'V'  :  5,
        'X'  :  10,
        'L'  :  50,
        'C'  :  100,
        'D'  :  500,
        'M'  :  1000}
        
    for x in num:
        if x  in d:
            val+=d[x]

    return val
    

num=input("enter:")
print(roman(num))
"""
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Solution:
    def romanToInt(self, S: str) -> int:
        summ= 0
        for i in range(len(S)-1,-1,-1):
            num = roman[S[i]]
            if 3*num < summ: 
                summ = summ-num
            else: 
                summ = summ+num
        return summ
    
obj=Solution()
num=input("enter:")
print(obj.romanToInt(num))