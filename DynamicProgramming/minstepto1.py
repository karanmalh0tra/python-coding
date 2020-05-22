import sys
def minStep(n, dp): #Recursive O(n) instead of O(2^n)
    if n == 1:
        return 0
    if dp[n-1] != -1:
        ans1 = dp[n-1]
    else:
        ans1 = minStep(n-1,dp)
        dp[n-1] = ans1
    ans2 = sys.maxsize
    if n % 2 == 0:
        if dp[n//2] != -1:
            ans2 = dp[n//2]
        else:
            ans2 = minStep(n/2,dp)
            dp[n//2] = ans2
    ans3 = sys.maxsize
    if n % 3 == 0:
        if dp[n//3] != -1:
            ans3 = dp[n//3]
        else:
            ans3 = minStep(n/3,dp)
            dp[n//3] = ans3
    return 1 + min(ans1,ans2,ans3)


def minStepTo1Iteratively(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    i = 4
    while(i<=n):
        ans1 = dp[i-1]
        ans2 = sys.maxsize
        ans3 = sys.maxsize
        if i % 2 == 0:
            ans2 = dp[i//2]
        if i % 3 == 0:
            ans3 = dp[i//3]
        dp[i] = 1 + min(ans1,ans2,ans3)
        i = i + 1
    return dp[n]

n = int(input())
#dp = [-1 for i in range(n+1)]
#ans = minStep(n,dp)
ans = minStepTo1Iteratively(n)
print(ans)
