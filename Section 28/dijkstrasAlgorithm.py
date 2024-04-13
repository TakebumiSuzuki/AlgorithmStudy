class PriorityQueue:
    def __init__(self):
        self.values = []
    def enqueue(self, val, priority):
        self.values.append({'val': val, 'priority': priority})
        self.sort()
    def dequeue(self):
        return self.values.pop(0)
    def sort(self):
        self.values.sort(key=lambda x: list(x.values())[1])
        

class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}
        
    def addVertex(self, vertex):
        if vertex not in self.adjacencyList :
            self.adjacencyList[vertex] = []
    
    def addEdge(self, vertex1, vertex2, weight):
        self.adjacencyList[vertex1].append({'node': vertex2, 'weight': weight})
        self.adjacencyList[vertex2].append({'node': vertex1, 'weight': weight})
               
    def Dijkstra(self, start, finish): #自分で作ってみたところQueueを使わない方法でできたが、この方法だたfor item節のところで余計な計算が必要となる
        distances = {}
        for key in self.adjacencyList.keys():
            distances[key] = float('inf')
        distances[start] = 0
        
        visited = set()
        comeFrom = {}
        currentLoc = start
        
        while True:
            if currentLoc == finish:
                break
            for nextLocNode in self.adjacencyList[currentLoc]:
                nextLoc = nextLocNode['node']
                weight = nextLocNode['weight']
                
                if (distances[currentLoc] + weight) < distances[nextLoc]:
                    distances[nextLoc] = distances[currentLoc] + weight
                    comeFrom[nextLoc] = currentLoc
                    
            minValue = float('inf')
            loc = ""
            for item in distances.items():
                if item[0] in visited:
                    continue
                if item[1] < minValue:
                    minValue = item[1]
                    loc = item[0]
            currentLoc = loc
            visited.add(currentLoc)
            
            
    def Dijkstra2(self, start, finish):
        nodes = PriorityQueue()
        distances = {}
        for key in self.adjacencyList.keys():
            distances[key] = float('inf')
        distances[start] = 0
        
        visited = set()
        previous = {}
        currentLoc = start
        
        while True:
            if currentLoc == finish:
                break
            for nextLocNode in self.adjacencyList[currentLoc]:
                nextLoc = nextLocNode['node']
                weight = nextLocNode['weight']
                
                if (distances[currentLoc] + weight) < distances[nextLoc]:
                    distances[nextLoc] = distances[currentLoc] + weight
                    previous[nextLoc] = currentLoc
            
            visited.add(currentLoc)
            for item in distances.items():   
                if item[0] in visited:
                    continue
                nodes.enqueue(item[0], item[1]) 
            currentLoc = nodes.dequeue()['val']
                  
        
        
    def Dijkstra3(self, startName, finishName): #講義での方法、結局nodesQueueの中の数字の大きい情報を残したまま終わるっている
        nodesQueue = PriorityQueue()
        comeFromDic = {}
        distancesDic = {}
        nearestNodeName = ''
        path = []
        
        for nodeName in self.adjacencyList.keys(): #adjacencyListは{ "A": {'node' : "B", 'weight' : 4}, {'node' : "C", 'weight' : 5}, "B": {....}}などの形式になっている
            if nodeName == startName:
                distancesDic[nodeName] = 0
                nodesQueue.enqueue(nodeName, 0)
            else:
                distancesDic[nodeName] = float('inf')
                nodesQueue.enqueue(nodeName, float('inf'))
            comeFromDic[nodeName] = None
        
        while len(nodesQueue.values) != 0:
            nearestNodeName = nodesQueue.dequeue()['val']
            if nearestNodeName == finishName:
                while comeFromDic[nearestNodeName] is not None:
                    path.append(nearestNodeName)
                    nearestNodeName = comeFromDic[nearestNodeName]
                break
                    
                    
            if (nearestNodeName is not None) or (distancesDic[nearestNodeName] != float('inf')):
                for neighborNodeDic in self.adjacencyList[nearestNodeName]:
                    neighborName = neighborNodeDic['node']
                    candidate = distancesDic[nearestNodeName] + neighborNodeDic['weight']
                    
                    if candidate < distancesDic[neighborName]:
                        distancesDic[neighborName] = candidate
                        comeFromDic[neighborName] = nearestNodeName
                        nodesQueue.enqueue(neighborName,candidate)
        #enqueueした状態でwhile節を終える、そしてwhile節の最初でdequeueする
        
        path = (path + [startName])
        path.reverse()#このreverse関数は戻り値はNoneになり、pathそのものを変更しているので使い方を間違えやすい
        return path
        

g = WeightedGraph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")

g.addEdge("A", "B", 4)
g.addEdge("A", "C", 2)
g.addEdge("B", "E", 3)
g.addEdge("C", "D", 2)
g.addEdge("C", "F", 4)
g.addEdge("D", "E", 3)
g.addEdge("D", "F", 1)
g.addEdge("E", "F", 1)

print(g.Dijkstra3("A", "E"))
