import math,sys
def minSquaresToN(n):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1,root+1):
        currAns = 1 + minSquaresToN(n-(i**2))
        ans = min(ans,currAns)
    return ans

def minSquaresToNMemoization(n,dp): #Memoization
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root+1):
        newCheckValue = n-(i**2)
        if dp[newCheckValue] == -1:
            smallAns = minSquaresToNMemoization(newCheckValue,dp)
            dp[newCheckValue] = smallAns
            currAns = 1 + smallAns
        else:
            currAns = 1 + dp[newCheckValue]
        ans = min(ans, currAns)
    return ans

def minSquaresToNIterative(n): #Dynamic Problem
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(1,n+1):
        root = int(math.sqrt(i))
        ans = sys.maxsize
        for j in range(1,root+1):
            currAns = 1 + dp[i-(j**2)]
            ans = min(ans,currAns)
        dp[i] = ans
    return dp[n]

n = int(input())
#dp = [-1 for i in range(n+1)]
ans = minSquaresToNIterative(n)
print(ans)
