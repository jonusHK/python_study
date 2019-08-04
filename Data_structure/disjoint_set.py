# Union Find Algorithm
class DisjointSet:
   def __init__(self, vnum):
       self.parent = [-1 for _ in range(vnum)]

   def simple_find(self, i):
       # i가 속한 트리의 루트를 반환
       while self.parent[i] >= 0:
           i = self.parent[i]
       return i

   def simple_union(self, i, j):
       # i, j must be ROOTS
       self.parent[i] = j

   # 성능 향상
   # 노드의 개수대로 root의 음수 값을 변경한다,(노드가 3개라면 -3)
   def collapsing_find(self, i):
       root = i
       while self.parent[root] >= 0:
           root = self.parent[root]

       trail = i

       while trail != root:
           lead = self.parent[trail]
           self.parent[trail] = root
           trail = lead

       return root

   def weighted_union(self, i, j):
       # i, j must be ROOTS
       temp = self.parent[i] + self.parent[j]
       if self.parent[i] > self.parent[j]:
           self.parent[i] = j
           self.parent[j] = temp
       else:
           self.parent[j] = i
           self.parent[i] = temp

if __name__ == "__main__":
    ds = DisjointSet(5)

    ds.parent[2] = -5
    ds.parent[4] = 2
    ds.parent[0] = 4
    ds.parent[1] = 0
    ds.parent[3] = 1

    print(ds.parent)
    print("the root is {}".format(ds.collapsing_find(3)))
    print(ds.parent)
