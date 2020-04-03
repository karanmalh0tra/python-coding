def tripletsum(arr, sum):
    arr.sort()  # hoping it is merge sort
    length = len(arr)
    for i in range(length - 2):
        j = i + 1
        k = length - 1
        while j < k:
            if arr[i] + arr[j] + arr[k] == sum:
                leftcount = 1
                l = 1
                while j+l <= length-1 and arr[i] + arr[j + l] + arr[k] == sum:
                    leftcount = leftcount + 1
                    l = l + 1
                rightcount = 1
                r = 1
                while k-r >= 0 and arr[i] + arr[j] + arr[k - r] == sum:
                    r = r + 1
                    rightcount = rightcount + 1
                if ((arr[j] == arr[k]) and (arr[i] + arr[j] + arr[k] == sum)):
                    sumtask = 0
                    for task in range(leftcount):
                        sumtask = sumtask + task
                    for _ in range(sumtask):
                        print (arr[i], arr[j], arr[k])
                else:
                    for _ in range(leftcount * rightcount):
                        print (arr[i], arr[j], arr[k])
                j = j + leftcount
                k = k - rightcount
            elif arr[i] + arr[j] + arr[k] <= sum:
                j = j + 1
            else:
                k = k - 1


## Read input as specified in the question.
## Print output as specified in the question.
l = input()
arr = [int(x) for x in input().strip().split()]
sum = int(input())
tripletsum(arr,sum)
