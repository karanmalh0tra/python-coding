class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def length(head):
    count = 0
    while head is not None:
        count = count + 1
        head = head.next
    return count

def delete(head, i):
    #############################
    if i < 0 or i >= length(head):
        return head
    prev = None
    curr = head
    count = 0
    while count < i:
        prev = curr
        curr = curr.next
        count = count + 1
    if prev is not None:
        prev.next = curr.next
        curr.next = None
    else:
        head = curr.next
    return head

def insertAtI(head,i,data):
    if i < 0 or i > length(head):
        return head
    prev = None
    curr = head
    count = 0
    while count < i:
        prev = curr
        curr = curr.next
        count = count + 1
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr

    return head

def insertAtIRecursively(head,i,data):
    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    if head is None: #should be below i == 0  condition.
        return None

    smallHead = insertAtIRecursively(head.next,i-1,data)
    head.next = smallHead
    return head

def deleteRecursively(head, i):
    if i == 0:
        head = head.next
        return head

    if head.next is None:
        return head

    head.next = deleteRecursively(head.next,i-1)
    return head

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end = " ")
        head = head.next
    print("None")

head = takeInput()
printLL(head)
head = insertAtI(head,2,6)
head = insertAtI(head,0,9)
printLL(head)
head = delete(head,0)
printLL(head)
