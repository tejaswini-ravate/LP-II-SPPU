from collections import deque

def bfs(adj):
    V = len(adj)
    res = []
    s = 0  

    q = deque()
    visited = [False] * V
    visited[s] = True
    q.append(s)

    while q:
        curr = q.popleft()
        res.append(curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return res

if __name__ == "__main__": 
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    adj = [[] for _ in range(V)]

    print("Enter edges (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    print("\nBFS traversal is:")
    ans = bfs(adj)
    for i in ans:
        print(i, end=" ")
