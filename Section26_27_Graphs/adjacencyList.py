class Graph:
    def __init__(self):
        self.adjacencyList = {}
        
    def addVertex(self, vertex):
        self.adjacencyList[vertex] = []
    
    def addEdge(self, v1, v2):
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)
    
    def removeEdge(self, v1, v2):
        self.adjacencyList[v1].remove(v2)
        self.adjacencyList[v2].remove(v1)
        
    def removeVertex(self, vertex):
        edgeList = self.adjacencyList[vertex].copy() #ポインタ問題を回避するためにcopy()する。でないと次のfor Loopがうまくいかない
        for edge in edgeList:
            self.adjacencyList[edge].remove(vertex)
            self.adjacencyList[vertex].remove(edge)
        self.adjacencyList.pop(vertex)
        
    def removeVertex2(self, vertex):
        edgeList = self.adjacencyList[vertex]
        for edge in edgeList:
            self.adjacencyList[edge].remove(vertex)
        self.adjacencyList.pop(vertex)
        
    def DFS_recursive(self, start):
        if start not in self.adjacencyList: return None
        visited = {}
        result = []
        
        def recursive(vertex):
            result.append(vertex)
            visited[vertex] = True 
            for neighbor in self.adjacencyList[vertex]:
                if neighbor in visited and visited[neighbor] == True:
                    continue
                else:
                    recursive(neighbor)
            
        recursive(start)
        return result
    
    
    #自力バージョン。自力で考えたhistoryの論理が劣っている(stackと言う論理を使った方がシンプル)ので下の動画解説バージョンの方が良い。
    def DFS_iterative(self, start):
        visited = {}
        result = []
        history = []
        currentVertex = start
        
        while True:
            neighborsList = self.adjacencyList[currentVertex]
            temp = currentVertex
            for neighbor in neighborsList:
                if neighbor in visited and visited[neighbor] == True:
                    continue
                else:
                    if currentVertex not in result:
                        result.append(currentVertex)
                    history.append(currentVertex)
                    visited[currentVertex] = True
                    currentVertex = neighbor
                    break
            
            if currentVertex == temp:
                if len(history) == 0:
                    return result
                else:
                    if currentVertex not in result:
                        result.append(currentVertex)
                    visited[currentVertex] = True
                    prevVertex = history.pop()
                    currentVertex = prevVertex
    
    
    #動画解説バージョン。まだ訪れてないvertexに対してもvisitedとしてしまうので直感的ではない論理となっていてわかりづらい
    def DFS_iterative2(self, start):
        stack = [start]
        result = []
        visited = {}
        currentVertex = ""
        
        visited[start] = True
        while len(stack) != 0:
            currentVertex = stack.pop()
            result.append(currentVertex)
            
            for neighbor in self.adjacencyList[currentVertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)
                    
        return result
    
    
    #自力バージョン。動画のバージョンは上のDFS_iterative2と同様まだ訪れてなくてもvisitedとしてしまうので直感的ではない。
    #よって、この自力バージョンの方がわかりやすい書き方かなと。なお、BFS方式(水平に処理していく)方法はrecursiveは使えない。
    #recursiveが使えるのはDFS方式のみと思われたがコメントを見るとrecursiveも可能な模様
    def BFS_iterative(self, start):
        result = []
        visited = {}
        queue = []
        currentVertex = start
        
        while True:
            visited[currentVertex] = True
            result.append(currentVertex)
            for neighbor in self.adjacencyList[currentVertex]:
                if neighbor in visited and visited[neighbor] == True:
                    continue
                else:
                    if neighbor not in queue:
                        queue.append(neighbor)
            
            if queue == []:
                return result
            else:
                currentVertex = queue.pop(0)
                    
        
    
        
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

print(g.BFS_recursive("A"))


    
    
    
    