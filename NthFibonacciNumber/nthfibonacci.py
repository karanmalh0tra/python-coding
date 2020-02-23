n = int(input())
previousfib = 1
lastfib = 1
fib = 0
i = 3
if n == 1:
    print("1")
elif n == 2:
    print("1")
else:
    while(i<=n):
        fib = lastfib + previousfib
        previousfib = lastfib
        lastfib = fib
        i = i + 1
    print(fib)
