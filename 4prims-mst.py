import heapq

def tree(V, E, edges):
    adj = [[] for _ in range(V)]

    for u, v, wt in edges:
        adj[u].append((v, wt))
        adj[v].append((u, wt))

    def prim(start, visited):
        pq = [(0, start)] 
        total = 0

        while pq:
            wt, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            total += wt

            for v, weight in adj[u]:
                if not visited[v]:
                    heapq.heappush(pq, (weight, v))

        return total

    res = 0
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            res += prim(i, visited)
    return res

if __name__ == "__main__":
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    edges = []
    print("Enter the edges in format u v wt:")
    for _ in range(E):
        u, v, wt = map(int, input().split())
        edges.append([u, v, wt])

    res = tree(V, E, edges)
    print("Total weight is:", res)
