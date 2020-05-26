import sys
def minCostRecursive(cost,i,j,m,n):
    #Special Case
    if i == m-1 and j==n-1:
        return cost[i][j]
    
    #Base Case
    if i >= m or j>=n:
        return sys.maxsize
    ans1 = minCostRecursive(cost,i,j+1,m,n)
    ans2 = minCostRecursive(cost,i+1,j,m,n)
    ans3 = minCostRecursive(cost,i+1,j+1,m,n)
    my_cost = cost[i][j] + min(ans1,ans2,ans3)
    return my_cost

def minCostMemoization(cost,i,j,m,n,dp):
    #Special Case
    if i == m-1 and j==n-1:
        return cost[i][j]
    
    #Base Case
    if i >= m or j>=n:
        return sys.maxsize
    if dp[i][j+1] == sys.maxsize:
        ans1 = minCostMemoization(cost,i,j+1,m,n,dp)
        dp[i][j+1] = ans1
    else:
        ans1 = dp[i][j+1]
    if dp[i+1][j] == sys.maxsize:
        ans2 = minCostMemoization(cost,i+1,j,m,n,dp)
        dp[i+1][j] = ans2
    else:
        ans2 = dp[i+1][j]
    if dp[i+1][j+1] == sys.maxsize:
        ans3 = minCostMemoization(cost,i+1,j+1,m,n,dp)
        dp[i+1][j+1] = ans3
    else:
        ans3 = dp[i+1][j+1]
    my_cost = cost[i][j] + min(ans1,ans2,ans3)
    return my_cost

cost = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
m = 4
n = 3
dp = [[sys.maxsize for j in range(n+1)] for i in range(m+1)]
#ans = minCostRecursive(cost,0,0,4,3)
ans = minCostMemoization(cost,0,0,4,3,dp)
print(ans)

#   1   5   11
#   8   13  12
#   2   3   7
#   15  16  18
# 1+8+3+18 = 30