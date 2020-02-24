def pushZeroesToEnd(arr):
    length = len(arr)
    count = 0
    for i in range(0,length):
        if arr[i] != 0:
            arr[count] = arr[i]
            count = count + 1
    while count < length:
        arr[count] = 0
        count = count + 1




## Read input as specified in the question.
n = int(input())
arr = [int(x) for x in input().strip().split(' ')]
pushZeroesToEnd(arr)
## Print output as specified in the question.
print(*arr)
