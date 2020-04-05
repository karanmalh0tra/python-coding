class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def merge(h1,h2):
    if h1 is None:
        return h2
    elif h2 is None:
        return h1
    if h1.data <= h2.data:
        comb = h1
        h1 = h1.next
    else:
        comb = h2
        h2 = h2.next
    prev = comb
    while h1 is not None and h2 is not None:
        if h1.data <= h2.data:
            comb.next = h1
            h1 = h1.next
            comb = comb.next
        else:
            comb.next = h2
            h2 = h2.next
            comb = comb.next
    if h1 is not None:
        comb.next = h1
    if h2 is not None:
        comb.next = h2
    return prev

def mergeSort(head):
    #  Sort a given linked list using Merge Sort.
    #############################
    if head.next is None or head is None:
        return head
    fast = head
    mid = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        mid = mid.next
    head1 = head
    head2 = mid.next
    mid.next = None
    h1 = mergeSort(head1)
    h2 = mergeSort(head2)
    return merge(h1,h2)
    #############################

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)
