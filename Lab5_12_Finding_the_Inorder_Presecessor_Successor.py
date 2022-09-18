#Finding the Inorder Predecessor and Successor
#A BST node
class Node(object):
    # Constructor to create a new node
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None

    # for finding the predecessor and successor of the node
    def findPredecessorAndSuccessor(self, data):
        global predecessor, successor
        predecessor = None
        successor = None

        if self is None:
            return

        # if the data is in the root itself
        if self.data == data:
            # the maximum value in the left subtree is the predecessor
            if self.left is not None:
                temp = self.left
                if temp.right is not None:
                    while(temp.right):
                        temp = temp.right
                predecessor = temp

            # the minimum of the right subtree is the successor
            if self.right is not None:
                temp = self.right
                while(temp.left):
                    temp = temp.left
                successor = temp

            return

        #if key is smaller than root, go to left subtree
        if data < self.data:
            print('Left')
            self.left.findPredecessorAndSuccessor(data)
        else:
            print('Right')
            self.right.findPredecessorAndSuccessor(data)

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

if __name__ == '__main__':
    root = Node(90)
    root.insert(70)
    root.insert(60)
    root.insert(80)
    root.insert(110)
    root.insert(100)
    root.insert(120)

    # following BST is created
    #               90
    #            /     \
    #           70     110
    #          /  \    /  \
    #        60   80 100  110

    root.findPredecessorAndSuccessor(70)
    if  (predecessor is not None) and (successor is not None):
        print('Predecessor:', predecessor.data, 'Successor:', successor.data)
    else:
        print('Predecessor:', predecessor, 'Successor:', successor)
