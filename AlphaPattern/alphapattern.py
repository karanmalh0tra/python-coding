N = int(input())
if N == 0:
    print()
else:
    i = 1
    while(i<=N):
        j = 1
        startchar = chr(ord('A')+i-1)
        while(j<=i):
            print(startchar,end="")
            j = j + 1
        print()
        i = i + 1
