def partition(arr,start,end):
    count = 0
    pivot = arr[start]
    for i in range(start,end+1):
        if arr[i] < pivot:
            count = count + 1
    arr[start],arr[start+count] = arr[start+count],arr[start]
    pivot_index = start+count
    i = start
    j = end
    while i<j:
        if arr[i] < pivot:
            i = i + 1
        elif arr[j] >= pivot:
            j = j - 1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
    return pivot_index

def quickSort(arr, start, end):
    if start >= end:
        return
    pivot_index = partition(arr,start,end)
    quickSort(arr,start,pivot_index-1)
    quickSort(arr,pivot_index+1,end)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
