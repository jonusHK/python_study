# n개의 큰 도시가 있다.
# 어떤 세일즈맨이 모든 도시를 한번씩만 방문한 뒤 다시 돌아오려고 한다.
# 모든 경로 중 가장 짧은 경로를 구하시오.
import math


n = 5
dist = [
    [0, 2, 5, 3, 7],
    [2, 0, 10, 6, 6],
    [5, 10, 0, 4, 8],
    [3, 6, 4, 0, 12],
    [7, 6, 8, 12, 0]
]

### Brtue Force Search
path = []
visited = [False for _ in range(n)]

# shortest_path1(path, visited, d) -> length
# 이미 거쳐 온 경로 path, 방문한 도시를 나타내는 visited, 지금까지의 길이 d가 주어질 때 최단 경로의 길이
def shortest_path1(path, visited, d):
    # base case
    # all(visited) == True
    # sumation of edges

    if all(visited):
        return d+dist[path[-1]][path[0]]


    cur = path[-1]

    ret = math.inf
    for _next in range(n):
        if not visited[_next]:
            path.append(_next)
            visited[_next] = True
            ret = min(ret, shortest_path1(path, visited, d+dist[cur][_next]))
            path.pop()
            visited[_next] = False

    return ret


path.append(0)
visited[0] = True



### Dynamic Programming
cache = [[None for _ in range(1<<n)] for _ in range(n)]
# 여기서 나올 수 없는 최대한의 큰 값으로 설정
INF = 99999

# 0부터 시작한다고 가정
# shortest_path2(cur, visited) -> length
# 현재 위치 cur 방문한 도시들 visited일 때 남은 도시를 방문하는 최소 경로의 길이
def shortest_path2(cur, visited):
    # base case
    # 모두 방문했다면 처음과 끝의 경로의 길이
    if visited == (1<<n)-1:
        return dist[cur][0]

    if cache[cur][visited] != None:
        return cache[cur][visited]

    cache[cur][visited] = INF
    for _next in range(n):
        # 아직 _next를 방문하지 않았다면
        if not (visited & (1<<_next)):
            cache[cur][visited] = \
            min(cache[cur][visited], dist[cur][_next]+shortest_path2(_next, visited+(1<<_next)))

    return cache[cur][visited]


if __name__ == "__main__":
    print(shortest_path1(path, visited, 0))
    print(shortest_path2(0, 1))