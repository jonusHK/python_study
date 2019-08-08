class ShortestPath:
    def __init__(self, src, dist, p):
       self.source = src
       self.distance = dist
       # predecessor
       self.p = p

    def print_path(self, dst):
        # 1. base case
        if self.source == dst:
            print(self.source, end="  ")
            return
        if self.p[dst] != None:
            self.print_path(self.p[dst])
        else:
            print("There is no path")
            return

        # 2. recursion case
        self.print_path()
        print(dst, end=" ")

class Graph:
    INF = 99999
    def __init__(self, vnum):
        self.adjacency_matrix = [[None for _ in range(vnum)] for _ in range(vnum)]
        self.vertex_num = vnum

    def insert_edge(self, u, v, w):
        self.adjacency_matrix[u][v] = w

    def find_min(self, distance, S):
        _min = Graph.INF
        min_v = None

        for v in range(self.vertex_num):
            if v not in S and distance[v] < _min:
                _min = distance[v]
                min_v = v
        return min_v


    def dijkstra(self, src):
        S = set()
        # distance = [math.inf for _ in range(self.vertex_num)]
        distance = [Graph.INF for _ in range(self.vertex_num)]
        p = [None for _ in range(self.vertex_num)]

        distance[src] = 0

        while len(S) < self.vertex_num:
            v = self.find_min(distance, S)
            S.add(v)

            # adj[v] 구하기
            for u in range(self.vertex_num):
                w = self.adjacency_matrix[v][u]

                # 핵심!!
                # w != None --> adj[v] 안에 u가 포함
                # u not in S -> u는 아직 S 안에 미포함
                # RELAXATION : if distance[u] > distance[v] + w then distance[u] = distance[v] + w
                if w != None and u not in S and distance[u] > distance[v] + w:
                    distance[u] = distance[v] + w
                    p[u] = v

        return ShortestPath(src, distance, p)



if __name__=="__main__":
   g = Graph(4)
   g.insert_edge(0, 1, 10)
   g.insert_edge(0, 2, 3)
   g.insert_edge(1, 3, 5)
   g.insert_edge(2, 1, 5)
   g.insert_edge(2, 3, 8)
   g.insert_edge(3, 1, 4)
   g.insert_edge(3, 2, 12)

   source=0
   sp=g.dijkstra(source)
   for i in range(g.vertex_num):
       print('distance[{0}] : {1}, p[{0}] : {2}'.format(i, sp.distance[i], sp.p[i]))