def knapsackRecursive(W,val,wt,n,i):

    if i == n: #Base Case
        return 0

    if wt[i] > W:
        ans = knapsackRecursive(W,val,wt,n,i+1)
    else:
        ans1 = val[i] + knapsackRecursive(W-wt[i], val,wt,n,i+1) #inclusion of i'th item
        ans2 = knapsackRecursive(W,val,wt,n,i+1) #exclusion of i'th item
        ans = max(ans1,ans2)
    return ans

def knapsack(W,val,wt): #Dynamic Programming
    n = len(val)
    dp = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,W+1):
            if j < wt[i-1]:
                ans = dp[i-1][j]
            else:
                ans1 = val[i-1] + dp[i-1][j-wt[i-1]]
                ans2 = dp[i-1][j]
                ans = max(ans1,ans2)
            dp[i][j] = ans
    return dp[n][W]


val = [200,300,100]
wt = [20,25,30]
W = 50
n = len(val)
ans = knapsack(W,val,wt)
print(ans)