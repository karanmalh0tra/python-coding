def wavePrint(arr):
    count = 0
    for j in range(len(arr[0])):
        if count % 2 == 0:
            for i in range(len(arr)):
                print(arr[i][j],end=" ")
            count = count + 1
        else:
            for i in range(len(arr)-1,-1,-1):
                print(arr[i][j],end=" ")
            count = count + 1

#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
wavePrint(arr)
