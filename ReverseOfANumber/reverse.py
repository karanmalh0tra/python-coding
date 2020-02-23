def reverse(n):
#Implement Your Code Here
    rev = 0
    while(n!=0):
        r = n%10
        rev = rev*10 + r
        n = n // 10
    return(rev)


n=int(input())
result = reverse(n)
print(result)
