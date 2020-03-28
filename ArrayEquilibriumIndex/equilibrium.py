def equilibriumIndex(arr):
    l = len(arr)
    index = 0
    i = 1
    sum_on_left = 0
    sum_on_right = 0
    while i < l:
        sum_on_right = sum_on_right + arr[i]
        i = i + 1
    i = 1
    while i < l:
        sum_on_left = sum_on_left + arr[i-1]
        sum_on_right = sum_on_right - arr[i]
        if sum_on_left == sum_on_right:
            return i
        i = i + 1
    return -1

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))
