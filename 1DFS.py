def dfs_util(curr, visited, adj, res):
    visited[curr] = True
    res.append(curr)

    for neighbor in adj[curr]:
        if not visited[neighbor]:
            dfs_util(neighbor, visited, adj, res)

def dfs(adj):
    V = len(adj)
    res = []
    visited = [False] * V
    dfs_util(0, visited, adj, res)
    return res

if __name__ == "__main__":  
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    adj = [[] for _ in range(V)]

    print("Enter edges (space-separated u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    print("\nDFS traversal is:")
    ans = dfs(adj)
    for i in ans:
        print(i, end=" ")
