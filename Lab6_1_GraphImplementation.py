#Lab6.1 Graph implementation in Python using Adjacency List
class AdjacencyList(object):
    def __init__(self):
        self.List = {}

    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present
        if fromVertex in self.List.keys():
            self.List[fromVertex].append(toVertex)
        else:
            self.List[fromVertex] = [toVertex]

    def printList(self):
        for i  in self.List:
            print(i,'->',' -> '.join([str(j) for j in self.List[i]]))

if __name__ == '__main__':
    g = AdjacencyList()
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(4, 1)
    g.addEdge(4, 3)
    g.addEdge(1, 0)
    g.addEdge(1, 4)
    g.addEdge(1, 3)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)

    g.printList()
