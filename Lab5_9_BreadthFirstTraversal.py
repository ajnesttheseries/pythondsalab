#Lab 5.9 Breadth First Traversal
class Node(object):
    def __init__(self, data = None):
        self.leftChild = None
        self.rightChild = None
        self.data = data

def height(node):
    if node is None:
        return 0
    else:
        leftHeight = height(node.leftChild)
        rightHeight = height(node.rightChild)

        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1

def breadthFirstTraversal(root):
    if root == None:
        return 0
    else:
        h = height(root)
        for i in range(1, h + 1):
            printBFT(root, i)

def printBFT(root, level):
    if root is None:
        return
    else:
        if level == 1:
            print(root.data, end = ' ')
        elif level > 1:
            printBFT(root.leftChild, level - 1)
            printBFT(root.rightChild, level - 1)

if __name__ == '__main__':
    root = Node('R')
    root.leftChild = Node('A')
    root.rightChild = Node('B')
    root.leftChild.leftChild = Node('C')
    root.leftChild.rightChild = Node('D')  
    root.leftChild.leftChild.leftChild = Node('F')    
    root.rightChild.leftChild = Node('E')
    root.rightChild.leftChild.leftChild = Node('G')
    root.rightChild.leftChild.rightChild = Node('H')
    
    breadthFirstTraversal(root)
