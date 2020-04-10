class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    #############################
    prevX = None
    currX = head
    count = 0
    while currX != None and count != i:
        prevX = currX
        currX = currX.next
        count = count+1
    prevY = None
    currY = head
    count = 0
    while currY!= None and count != j:
        prevY = currY
        currY = currY.next
        count = count + 1
    if prevX != None:
        prevX.next = currY
    else:
        head = currY
    if prevY != None:
        prevY.next = currX
    else:
        head = currX
    temp = currX.next
    currX.next = currY.next
    currY.next = temp

    return head
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
i, j=list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)
