"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
def profit(prices):
    
    minVal = 10000
    maxDiff = 0
        
    for i in range(len(prices)):
            minVal = min(prices[i], minVal)
            maxDiff = max(prices[i]-minVal, maxDiff)
            print(minVal,maxDiff)
            
    return maxDiff

prices=list(map(int,input().split()))
print(profit(prices))