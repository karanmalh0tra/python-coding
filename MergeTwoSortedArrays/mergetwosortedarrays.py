def mergeSortedArrays(arr1,arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    i = 0
    j = 0
    arr = []
    while((i<len1) and (j<len2)):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i = i + 1
        else:
            arr.append(arr2[j])
            j = j + 1
    while i<len1:
        arr.append(arr1[i])
        i = i + 1
    while j<len2:
        arr.append(arr2[j])
        j = j + 1
    return arr

## Read input as specified in the question.
m = int(input())
arr1 = [int(x) for x in input().strip().split(' ')]
n = int(input())
arr2 = [int(x) for x in input().strip().split(' ')]
arr = mergeSortedArrays(arr1,arr2)
## Print output as specified in the question.
print(*arr)
