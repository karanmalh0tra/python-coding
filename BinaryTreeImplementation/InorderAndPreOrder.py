import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePreOrder(preorder, inorder):
    # Given Preorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 12 Nodes with following input:
    # preOrder: 1 2 3 4 15 5 6 7 8 10 9 12
    # inOrder: 4 15 3 2 5 1 6 10 8 7 9 12
    #############################
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    root = BinaryTreeNode(preorder[0])
    i = 0
    for i in range(len(inorder)):
        if inorder[i] == preorder[0]:
            break
    leftinorder = inorder[:i]
    rightinorder = inorder[i+1:]
    leftpreorder = preorder[1:i+1]
    rightpreorder = preorder[i+1:]
    leftsubtree = buildTreePreOrder(leftpreorder,leftinorder)
    rightsubtree = buildTreePreOrder(rightpreorder,rightinorder)
    root.left = leftsubtree
    root.right = rightsubtree
    return root
    #############################

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
n=int(input())
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePreOrder(preorder, inorder)
printLevelATNewLine(root)

##Sample Input
# 12
# 1 2 3 4 15 5 6 7 8 10 9 12
# 4 15 3 2 5 1 6 10 8 7 9 12

##Sample Output (Level Wise)
# 1
# 2 6
# 3 5 7
# 4 8 9
# 15 10 12
