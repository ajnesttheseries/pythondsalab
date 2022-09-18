#Lab 5.7 Tree Implementation - Preorder, Inorder, and Postorder Traversals
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
# in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
def preorder(Tree):
    if Tree:
        print(Tree.getData(), end = ' ')
        preorder(Tree.getLeft())
        preorder(Tree.getRight())
    return
# in this we traverse first to the leftmost node, then print its data and then traverse for rightmost node
def inorder(Tree):
    if Tree:
        inorder(Tree.getLeft())
        print(Tree.getData(), end = ' ')
        inorder(Tree.getRight())
    return
# in this we first traverse to the leftmost node and then to the rightmost node and then print the data
def postorder(Tree):
    if Tree:
        postorder(Tree.getLeft())
        postorder(Tree.getRight())
        print(Tree.getData(), end = ' ')
    return

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
    
    print('Preorder Traversal:')
    preorder(root)
    print('\nInorder  Traversal:')
    inorder(root)
    print('\nPostorder Traversal:')
    postorder(root)

    """
    INPUT

              R
           /     \
          A       B
         / \     /
        C   D   E
       /       / \
      F       G   H
    

    OUTPUT:
    Preorder Traversal:
    R A C F D B E G H
    Inorder Traversal:
    F C A D R G E H B
    Postorder Traversal:
    F C D A G H E B R
    """
