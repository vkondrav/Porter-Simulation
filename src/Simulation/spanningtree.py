from dijkstra import dijkstra

class SpanningTree(object):

    def __init__(self, treeFile=None):
        self.adj = {}
        self.cost = {}
		
        if treeFile:
            # load tree from file
            pass

    def addNode(self, node):
        self.adj[node] = []
		
    def addEdge(self, src, dest, time):
        # adds a directional edge
        self.adj[src].append(dest)
        self.cost[(src, dest)] = time

    def addBiEdge(self, node1, node2, time):
        self.addEdge(node1, node2, time)
        self.addEdge(node2, node1, time)
		
    def getTimeBetween(self, src, dest):
        if src == dest:
            return 0
            
        _, time = dijkstra(self.adj, self.cost, src, dest)
        return time
		

def constructSampleTree(tree):
    #      1
    #     / \
    # 100/   \150
    #   /     \
    #  /       \
    # 0---------2
    #     200
    
    tree.addNode(0)
    tree.addNode(1)
    tree.addNode(2)
    tree.addBiEdge(0, 1, 100)
    tree.addBiEdge(1, 2, 150)
    tree.addBiEdge(2, 0, 200)
	
if __name__=='__main__':
    spanTree = SpanningTree()
    constructSampleTree(spanTree)
    print spanTree.getTimeBetween(0, 1)