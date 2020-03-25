def selectionSort(arr):
    length = len(arr)
    for i in range(0,length-1):
        minIndex = i
        for j in range(i+1,length):
            if(arr[j] < arr[minIndex]):
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]

arr = [int(x) for x in input().strip().split()]
selectionSort(arr)
print(*arr)
