"""
use to traverse graphs (binary tress are special graphs)
used in web crawling, social networking, networking, garbage collection
normally, you get the shortest path to somewhere with bfs

example rubiks cube
2x2x2 cube
vertex for each possible state of the cube: 8! X 3^8 = 264,539,520
you can divide by 24 symetry of the cube
you can divide by 3 because you can only get to those states by taking the cube apart
undirected graph, worst case can solve in 11 moves for 2x2x2 cubes, 20 for 3x3x3


to represent a graph, you have an array storing pointers to a linked list
all operation is Q(V+E)

algo:
- visit all nodes reachable from given s
- o(v+e) time
- look at the nodes reachable in 0 moves, then 1...
- avoid duplicates

BFS(s, Adj)
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]: adj is the array storing pointer of linked list
                if v not in level:
                    level[]=i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
"""


