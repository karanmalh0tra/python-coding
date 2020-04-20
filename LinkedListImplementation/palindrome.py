class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def check_palindrome(head) :
    fast = head
    slow = head
    rev = None
    flag = 1
    if head is None:
        return True
    while fast and fast.next:
        if not fast.next.next:
            flag = 0
            break
        fast = fast.next.next
        temp = slow
        slow = slow.next
        temp.next = rev
        rev = temp
    fast = slow.next
    slow.next = rev
    if flag:
        slow = slow.next
    while fast and slow:
        if fast.data != slow.data:
            return False
        fast = fast.next
        slow = slow.next
    return True


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
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")
