def Rotate(arr, d):
    # Please add your code here
    length = len(arr)
    for i in range(d):
        firstele = arr[0]
        for j in range(length-1):
            arr[j] = arr[j+1]
        arr[-1] = firstele


# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
Rotate(arr, d)
print(*arr)
