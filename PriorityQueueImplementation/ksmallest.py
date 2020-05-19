import heapq
def kSmallest(lst, k):
    #############################
    if lst == None:
        return
    li = lst[:k]
    heapq._heapify_max(li)
    for i in range(k,len(lst)):
        if lst[i] < li[0]:
            heapq._heapreplace_max(li,lst[i])
    return li
    #############################

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
for ele in ans:
    print(ele)
