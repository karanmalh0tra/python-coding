class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def printTree(root):
    #not a base case, but an edge case
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, ":", end="")
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTreeDetailed(child)

#How many children approach
def takeTreeInput():
    print("Enter root Data")
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    print("Enter number of children for ", rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root

def numNodes(root):
    #Edge Case. Not a base case
    if root == None:
        return 0
    count = 1
    for child in root.children:
        count = count + numNodes(child)
    return count

root = takeTreeInput()
printTree(root)
printTreeDetailed(root)
print(numNodes(root))
