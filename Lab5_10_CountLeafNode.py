#Lab 5.10 Count Leaf Nodes
class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    # for setting left node
    def setLeft(self, node):
        self.left = node

    # for setting right node
    def setRight(self, node):
        self.right = node

    # for getting the left node
    def getLeft(self):
        return self.left

    # for getting right node
    def getRight(self):
        return self.right

    # for setting data of a node
    def setData(self, data):
        self.data = data

    # for getting data of a node
    def getData(self):
        return self.data

def countLeafNodes(root):
    if root is None:
        return 0
    if(root.left is None and root.right is None):
        return 1
    else:
        return countLeafNodes(root.left) + countLeafNodes(root.right)

if __name__ == '__main__':
    root = Node('R')
    root.setLeft(Node('A'))
    root.setRight(Node('B'))    
    root.left.setLeft(Node('C'))
    root.left.setRight(Node('D'))
    root.left.left.setLeft(Node('F'))
    root.right.setLeft(Node('E'))
    root.right.left.setLeft(Node('G'))
    root.right.left.setRight(Node('H'))

    print('Count of leaf nodes:',countLeafNodes(root))
