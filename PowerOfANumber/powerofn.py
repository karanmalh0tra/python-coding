def pow_of_n(x,n):
    if n == 0:
        return 1
    return x * pow_of_n(x,n-1)

## Read input as specified in the question.
li = [int(x) for x in input().strip().split(' ')]
x = li[0]
n = li[1]
## Print output as specified in the question.
print(pow_of_n(x,n))
