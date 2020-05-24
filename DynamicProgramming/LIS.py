def LISRecursive(li,i,n):
    if i == n:
        return 0,0
    including_max = 1
    for j in range(i+1,n):
        if li[j] >= li[i]:
            further_including_max = LISRecursive(li,j,n)[0]
            including_max = max(including_max, 1+further_including_max)
    excluding_max = LISRecursive(li,i+1,n)[1]
    overall_max = max(including_max,excluding_max)
    return including_max, overall_max

def LISMemoization(li,i,n,dp): #Memoization
    if i == n:
        return 0,0
    including_max = 1
    for j in range(i+1,n):
        if li[j] >= li[i]:
            if dp[j] == -1:
                ans = LISMemoization(li,j,n,dp)
                dp[j] = ans
                further_including_max = ans[0]
            else:
                further_including_max = dp[j][0]
            including_max = max(including_max, 1+further_including_max)
    if dp[i+1] == -1:
        ans = LISMemoization(li,i+1,n,dp)
        dp[i+1] = ans
        excluding_max = ans[1]
    else:
        excluding_max = dp[i+1][1]
    overall_max = max(including_max,excluding_max)
    return including_max, overall_max

def LISIterative(li,n): #Dynamic Problem
    dp = [[0 for j in range(2)] for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        including_max = 1
        for j in range(i+1,n):
            if li[j] > li[i]:
                including_max = max(including_max, 1+dp[j][0])
        dp[i][0] = including_max
        excluding_max = dp[i+1][1]
        overall_max = max(including_max, excluding_max)
        dp[i][1] = overall_max
    return dp[0][1]


n = int(input())
li = [int(ele) for ele in input().split()]
#dp = [-1 for i in range(n+1)]
ans = LISIterative(li,n)
print(ans)