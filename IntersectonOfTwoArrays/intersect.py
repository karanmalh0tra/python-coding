def merge(a1,a2,arr):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i = i + 1
            k = k + 1
        else:
            arr[k] = a2[j]
            j = j + 1
            k = k + 1
    while i < len(a1):
        arr[k] = a1[i]
        k = k + 1
        i = i + 1
    while j < len(a2):
        arr[k] = a2[j]
        k = k + 1
        j = j + 1



def mergesort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr)//2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    mergesort(a1)
    mergesort(a2)
    merge(a1,a2,arr)


def intersection(arr1, arr2):
    mergesort(arr1)
    mergesort(arr2)
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i = i + 1
        elif arr2[j] < arr1[i]:
            j = j + 1
        else:
            print(arr1[i])
            i = i + 1
            j = j + 1

# Main
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
intersection(arr1, arr2)

#Sort the two arrays by merge sort. Takes nlogn complexity. Intersection then takes only n.
