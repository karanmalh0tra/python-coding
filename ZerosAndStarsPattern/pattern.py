## Read input as specified in the question.
N = int(input())
## Print output as specified in the question.
i = 1
while(i<=N):
    zerocount = 1
    while(zerocount <= i-1):
        print("0",end = "")
        zerocount = zerocount + 1
    print("*",end = "")
    zerocount = 1
    while(zerocount <= N-i):
        print("0",end="")
        zerocount = zerocount + 1
    print("*",end="")
    zerocount = 1
    while(zerocount <= N-i):
        print("0",end="")
        zerocount = zerocount + 1
    print("*",end="")
    zerocount = 1
    while(zerocount <= i-1):
        print("0",end = "")
        zerocount = zerocount + 1
    print()
    i = i + 1
