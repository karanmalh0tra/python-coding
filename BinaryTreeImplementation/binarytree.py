class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root == None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end =":")
    if root.left != None:
        print('L', root.left.data, end=",")
    if root.right != None:
        print('R', root.right.data, end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput(): #Vertical Input
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def numNodes(root):
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1 + leftCount + rightCount
    #Without the 1 added, the nodes dont get counted hence output would turn 0

def sumOfAllNodes(root):
    if root == None:
        return 0
    nodeCount = root.data
    leftSum = sumOfAllNodes(root.left)
    rightSum = sumOfAllNodes(root.right)
    return nodeCount + leftSum + rightSum

def largestData(root):
    if root == None:
        return -1 #ideally returned -infinity
    leftLargest = largestData(root.left)
    rightLargest = largestData(root.right)
    return max(leftLargest, rightLargest, root.data)

def countNodesGreaterThanX(root,x):
    if root == None:
        return 0
    count = 0
    if root.data > x:
        count += 1
    count = count + countNodesGreaterThanX(root.left,x)
    count = count + countNodesGreaterThanX(root.right,x)
    return count

def height(root):
    if root == None:
        return 0
    leftheight = height(root.left)
    rightheight = height(root.right)
    if leftheight >= rightheaight:
        return 1+leftheight
    else:
        return 1+rightheight

def numLeafNodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    numLeafLeft = numLeafNodes(root.left)
    numLeafRight = numLeafNodes(root.right)
    return numLeafLeft + numLeafRight

def printDepthK(root,k):
    if root == None:
        return
    if k == 0:
        print(root.data)
        return
    printDepthK(root.left,k-1)
    printDepthK(root.right,k-1)

def printDepthKV2(root,k,d=0):
    if root == None:
        return
    if k == d:
        print(root.data)
        return
    printDepthKV2(root.left,k,d+1)
    printDepthKV2(root.right,k,d+1)

def removeLeaves(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = removeLeaves(root.left)
    root.right = removeLeaves(root.right)
    return root

def mirrorBinaryTree(root):
    if root == None:
        return None
    root.left,root.right = mirrorBinaryTree(root.right),mirrorBinaryTree(root.left)
    return root

def isBalanced(root): #O(n^2) worst case and O(nlogn) best case.
#O(n * h) where h is the height.
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False

def getHeightAndCheckBalanced(root):
    if root == None:
        return 0, True
    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)

    h = 1 + max(lh,rh)
    if lh - rh > 1 or rh - lh > 1:
        return h, False
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False

import queue
def treeInputParralel(): #Use Queue
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root =  BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node = q.get()
        print("Enter left child of: ",current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter right child of: ",current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root

def printTreeDetailedParallel(root):
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    while(not(q.empty())):
        current_node = q.get()
        print(current_node.data,end=":")
        if current_node.left != None:
            q.put(current_node.left)
            print("L:" + str(current_node.left.data),end=",")
        else:
            print("L:-1",end=",")
        if current_node.right != None:
            q.put(current_node.right)
            print("R:" + str(current_node.right.data))
        else:
            print("R:-1")

root = treeInputParralel()
printTreeDetailed(root)
printTreeDetailedParallel(root)
