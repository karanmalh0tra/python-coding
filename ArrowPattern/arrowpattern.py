## Read input as specified in the question.
N = int(input())
## Print output as specified in the question.
i = 1
N1 = (N+1)//2
N2 = N//2
while(i<=N1):
    space = 1
    while(space<i):
        print(" ",end="")
        space = space + 1
    j = 1
    while(j<=i):
        print("*",end=" ")
        j = j + 1
    print()
    i = i + 1
i = 1
while(i<=N2):
    space = 1
    while(space<N2-i+1):
        print(" ",end="")
        space = space + 1
    j = 1
    while(j<=N2-i+1):
        print("*",end=" ")
        j = j + 1
    print()
    i = i + 1
