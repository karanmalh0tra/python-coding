def binarysearch(l,s):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end)//2
        if s > l[mid]:
            start = mid + 1
        elif s < l[mid]:
            end = mid - 1
        else:
            return mid
    return -1

## Read input as specified in the question.
n = int(input())
l = [int(x) for x in input().strip().split(' ')]
s = int(input())
## Print output as specified in the question.
print(binarysearch(l,s))
