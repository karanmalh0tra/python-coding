# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def midpoint_linkedlist(head):
    #  Given a linked list, find and return the midpoint.
    #############################
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow
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

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
node = midpoint_linkedlist(l)
if node:
    print(node.data)
