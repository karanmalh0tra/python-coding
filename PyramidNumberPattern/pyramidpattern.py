## Read input as specified in the question.
N = int(input())
## Print output as specified in the question.
i = 1
while(i<=N):
    space = 1
    while(space<=N-i):
        print(" ",end="")
        space = space + 1
    j = 1
    k = i
    while(j<=i):
        print(k,end="")
        k = k - 1
        j = j + 1
    k = 2
    j = 1
    while(j<i):
        print(k,end="")
        k = k + 1
        j = j + 1
    print()
    i = i + 1
