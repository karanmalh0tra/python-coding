import heapq
def checkMaxHeap(lst):
    #############################
    n = len(lst)
    for i in range(((n-2)//2)+1):
        if lst[2*i+1] > lst[i]:
            return False
        if (2*i+2 < n) and lst[2*i+2] > lst[i]:
            return False
    return True
    #############################

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
