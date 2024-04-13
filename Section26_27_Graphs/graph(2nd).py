class Graph:
    def __init__(self):
        self.adjacencyList = {}
        
    def addVertex(self, vertex):
        if vertex in self.adjacencyList: 
            print("The key already exists in the list: ", vertex)
            return
        self.adjacencyList[vertex] = []
        
    def addEdge(self, v1, v2):
        for i in [v1, v2]:
            if i not in self.adjacencyList:
                print("The key does not exists in the list yet: ", i)
                return
        self.adjacencyList[v1].append(v2) 
        self.adjacencyList[v2].append(v1)   
        
    def removeEdge(self, v1, v2):
        try:
            index1 = self.adjacencyList[v1].index(v2)
        except ValueError:
            print("element is not in the adjacencyList:",v1)
            return
        try:
            index2 = self.adjacencyList[v2].index(v1)
        except ValueError:
            print("element is not in the adjacencyList:", v2)
            return 
        
        del self.adjacencyList[v1][index1]
        del self.adjacencyList[v2][index2]
    
    def removeVertex(self, v):
        if v not in self.adjacencyList:
            print("このキーはそもそもadjacencyListに存在しません:", v)
            return
        deleteList = self.adjacencyList[v].copy()#ここでcopyをしないと、参照になるので下のforループで完全にループがされない
        for i in deleteList:
            self.removeEdge(i, v)
        del self.adjacencyList[v]
        
    def dfs_recursive(self, vertex):
        visitedDic = {}
        result = []
        
        def traverse(vertex):
            if vertex not in self.adjacencyList:
                return
            if vertex in visitedDic and visitedDic[vertex] == True:
                return
            visitedDic[vertex] = True
            result.append(vertex)
            for v in self.adjacencyList[vertex]:
                traverse(v)
                
        traverse(vertex)
        return result
    
    def dfs_iterative(self, vertex):#visitedQueueの辞書を定義し、煩わしいが、これがあることでO(1)のメリットを享受できる。ただし集合を使っても良い
        stackToVisit = [vertex]
        result = []
        visitQueue = {vertex : True}
        while stackToVisit != []:
            currentVertex = stackToVisit.pop()
            result.append(currentVertex)
            for v in self.adjacencyList[currentVertex]:
                if v not in visitQueue or visitQueue[v] != True:
                    visitQueue[v] = True
                    stackToVisit.append(v)
        return result
    
    def bfs_iterative(self, vertex):
        queue = [vertex]
        visited = {vertex : True}
        result = []
        while queue != []: #講義ではcurrentVertexをwhileの上で定義している。これは毎回インスタンス化する労力を避けるため
            currentVertex = queue.pop(0)
            result.append(currentVertex)
            for v in self.adjacencyList[currentVertex]:
                if v not in visited:
                    queue.append(v)
                    visited[v] = True
        return result
        
    
g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "E")
g.addEdge("D", "E")
g.addEdge("D", "F")
g.addEdge("E", "F")

print(g.bfs_iterative("A"))