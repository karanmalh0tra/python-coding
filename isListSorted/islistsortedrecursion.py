def isListSorted(a,si):
    l = len(a)
    if si == l-1 or si == l:
        return True
    if a[si] > a[si+1]:
        return False
    return isListSorted(a,si+1)

a = [int(x) for x in input().strip().split(' ')]
isListSorted(a,0)
