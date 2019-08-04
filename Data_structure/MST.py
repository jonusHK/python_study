from disjoint_set import DisjointSet

import math

# Graph representation : adjacency list
class GNode:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.link = None


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


class Graph:
    def __init__(self, vnum):
        self.adjacency_list = [None for _ in range(vnum)]
        self.edge_list = []
        self.vertex_num = vnum

    def __add__node(self, v, unode):
        cur = self.adjacency_list[v]
        if not cur:
            self.adjacency_list[v] = unode
            return
        while cur.link:
            cur = cur.link
        cur.link = unode

    def insert_edge(self, u, v, w):
        unode = GNode(u, w)
        vnode = GNode(v, w)

        self.__add__node(u, vnode)
        self.__add__node(v, unode)
        self.edge_list.append(Edge(u, v, w))

    def MST_kruskal(self):
        mst = Graph(self.vertex_num)
        ds = DisjointSet(self.vertex_num)
        self.edge_list.sort(key=lambda e: e.w)

        mst_edge_num = 0
        edge_idx = 0
        while mst_edge_num < self.vertex_num-1:
            edge = self.edge_list[edge_idx]
            if ds.collapsing_find(edge.u) != ds.collapsing_find(edge.v):
                mst.insert_edge(edge.u, edge.v, edge.w)
                ds.weighted_union(ds.collapsing_find(edge.u),
                                  ds.collapsing_find(edge.v))
                mst_edge_num += 1

            edge_idx += 1

        return mst

    def get_min_v(self, w):
        _min = math.inf
        # 가장 작은 vertex
        min_v = None
        for weight in w:
            for i in range(len(w)):
                if _min  > w[i]:
                    _min = w[i]
                    min_v = i
            return min_v

    def MST_prim(self):
        mst = Graph(self.vertex_num)
        TV = set()
        w = [math.inf for _ in range(self.vertex_num)]
        _from = [None for _ in range(self.vertex_num)]
        w[0] = 0
        while len(TV) < self.vertex_num:
            v = self.get_min_v(w)
            TV.add(v)
            if _from[v] != None:
                mst.insert_edge(v, _from[v], w[v])

            w[v] = math.inf
            u = self.adjacency_list[v]
            while u:
                if u.vertex not in TV and u.weight < w[u.vertex]:
                    w[u.vertex] = u.weight
                    _from[u.vertex] = v
                u = u.link


        return mst


    def print_edges(self):
        for edge in self.edge_list:
            print(f'({edge.u}, {edge.v}) : {edge.w}')


if __name__=="__main__":
    g = Graph(6)

    g.insert_edge(0, 1, 10)
    g.insert_edge(0, 2, 2)
    g.insert_edge(0, 3, 8)
    g.insert_edge(1, 2, 5)
    g.insert_edge(1, 4, 12)
    g.insert_edge(2, 3, 7)
    g.insert_edge(2, 4, 17)
    g.insert_edge(3, 4, 4)
    g.insert_edge(3, 5, 14)

    mst = g.MST_kruskal()
    mst = g.MST_prim()

    mst.print_edges()
