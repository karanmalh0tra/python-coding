def merge(a1,a2,arr):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            arr[k] = a1[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = a2[j]
            k = k + 1
            j = j + 1
    while i < len(a1):
        arr[k] = a1[i]
        k = k + 1
        i = i + 1
    while j < len(a2):
        arr[k] = a2[j]
        k = k + 1
        j = j + 1



def mergesort(arr):
    l = len(arr)
    mid = (l)//2
    if l == 0 or l == 1:
        return
    a1 = arr[:mid]
    a2 = arr[mid:]
    mergesort(a1)
    mergesort(a2)
    merge(a1,a2,arr)


def pairSum(arr, x):
    if len(arr) < 2:
        return
    mergesort(arr)
    left, right = 0, len(arr) - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == x:
            leftcount = 1
            i = 1
            while x == arr[left+i] + arr[right]:
                leftcount = leftcount + 1
                i = i + 1
            rightcount = 1
            j = 1
            while x == arr[left] + arr[right-j]:
                rightcount = rightcount + 1
                j = j + 1
            if arr[left] == arr[right]:
                sumtask = 0
                for task in range(leftcount):
                    sumtask = sumtask + task
                for i in range(sumtask):
                    print(arr[left], arr[right])
            else:
                for k in range(leftcount * rightcount):
                    print(arr[left], arr[right])
            left = left + leftcount
            right = right - rightcount
        elif currentSum < x:
            left = left + 1
        else:
            right = right - 1

# 1 2 2 3 3 4 4 5 6
# 2 2 2 2 2 2
# 5 => 10, 6 =>
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)
