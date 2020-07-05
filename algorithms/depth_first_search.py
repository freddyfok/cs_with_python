"""
recursively explore the graph, backtracking as necessary
it explores the whole graph until the answer is found

parent = {s: None}
DFS_visit(v, adj, s): #iterate from s
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_visit(v, adj, v)

DFS(v, adj): #iterate the choices of s
    parent = {}
    for s in v:
        if s not in parent:
            parent[s] = None
            DFS_visit(v, adj ,s)
"""