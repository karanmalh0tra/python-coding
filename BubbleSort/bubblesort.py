def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0,length - i - 1):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
## Read input as specified in the question.
n = int(input())
arr = [int(x) for x in input().strip().split(' ')]
bubbleSort(arr)
## Print output as specified in the question.
print(*arr)
