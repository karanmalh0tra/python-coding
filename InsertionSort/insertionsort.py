def insertionSort(arr):
    length = len(arr)
    for i in range(1,length): #first element to last element
        j = i - 1
        temp = arr[i]
        while(j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j= j-1
        arr[j + 1] = temp

## Read input as specified in the question.
n = int(input())
arr = [int(x) for x in input().strip().split(' ')]
insertionSort(arr)
print(*arr)
