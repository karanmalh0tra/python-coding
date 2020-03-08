def merge(a1,a2,a):
    i = 0
    j = 0
    k = 0
    while i<len(a1) and j<len(a2):
        if a1[i]<=a2[j]:
            a[k] = a1[i]
            i = i + 1
            k = k + 1
        else:
            a[k] = a2[j]
            j = j + 1
            k = k + 1
    while i<len(a1):
        a[k] = a1[i]
        i = i + 1
        k = k + 1
    while j<len(a2):
        a[k] = a2[j]
        j = j + 1
        k = k + 1

def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr)//2
    a1 = arr[:mid]
    a2 = arr[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a1,a2,arr)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
