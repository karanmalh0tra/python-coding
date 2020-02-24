def sumOfTwoArrays(arr1,arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    i = l1 - 1
    j = l2 - 1
    carry = 0
    if l1 > l2:
        arr3 = [0]*(l1+1)
        k = len(arr3) - 1
    else:
        arr3 = [0]*(l2+1)
        k = len(arr3) - 1
    while(i>=0 and j>=0):
        sum = carry + arr1[i] + arr2[j]
        if sum >= 10:
            arr3[k] = sum%10
            carry =  sum // 10
        else:
            arr3[k] = sum
            carry = 0
        i = i - 1
        j = j - 1
        k = k - 1

    while(i>=0):
        sum = carry + arr1[i]
        if sum >= 10:
            arr3[k] = sum%10
            carry =  sum // 10
        else:
            arr3[k] = sum
            carry = 0
        i = i - 1
        k = k - 1

    while(j>=0):
        sum = carry + arr2[j]
        if sum >= 10:
            arr3[k] = sum%10
            carry =  sum // 10
        else:
            arr3[k] = sum
            carry = 0
        j = j - 1
        k = k - 1
    arr3[k] = carry
    return arr3

## Read input as specified in the question.
n1 = int(input())
arr1 = [int(x) for x in input().strip().split(' ')]
n2 = int(input())
arr2 = [int(x) for x in input().strip().split(' ')]
## Print output as specified in the question.
print(*sumOfTwoArrays(arr1,arr2))
