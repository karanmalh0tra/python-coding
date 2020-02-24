def sortZeroOneTwo(arr):
    length = len(arr)
    nextZero = 0
    nextTwo = length - 1
    iter = 0
    while iter<=nextTwo:
        if arr[iter] == 0:
            arr[nextZero], arr[iter] = arr[iter],arr[nextZero]
            nextZero = nextZero + 1
            iter = iter + 1
        elif arr[iter] == 2:
            arr[nextTwo], arr[iter] = arr[iter],arr[nextTwo]
            nextTwo = nextTwo - 1
        else:
            iter = iter + 1

## Read input as specified in the question.
n = int(input())
arr = [int(x) for x in input().strip().split(' ')]
sortZeroOneTwo(arr)
## Print output as specified in the question.
print(*arr)
