#str1 and str2
#Find length of common subsequence

def lcsRecursive(str1,str2,i,j):
    if i == len(str1) or j == len(str2):
        return 0
    if str1[i] == str2[j]:
        ans = 1 + lcsRecursive(str1,str2,i+1,j+1)
    else:
        ans1 = lcsRecursive(str1,str2,i,j+1)
        ans2 = lcsRecursive(str1,str2,i+1,j)
        ans = max(ans1,ans2)
    return ans
    

str1 = "abedgjc"
str2 = "bmdgsc"
ans = lcsRecursive(str1,str2,0,0)
print(ans)