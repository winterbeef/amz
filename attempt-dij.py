#!/usr/bin/env python3

import heapq

class Node:
    def __init__(self):
        self.dist = float('inf')
        self.parent = None
        self.is_explored = False
    
    def newbest(self, parent, dist):
        self.parent = parent
        self.dist = dist

def dijkstra(graph, start):
    # node.dist == best from origin
    # graph[from][to] == edge distance

    nodes = {n:Node() for n in graph}
    nodes[start].newbest(parent=None, dist=0)

    minheap = [(0, start)]

    while minheap:
        curdist, cur = heapq.heappop(minheap)
        nodes[cur].is_explored = True

        for child, edge in graph[cur].items():
            if nodes[child].is_explored:
                continue

            newdist = curdist + edge
            if newdist < nodes[child].dist:
                nodes[child].newbest(parent=cur, dist=newdist)
                heapq.heappush(minheap, (newdist, child))
    
    return nodes

# Example Usage:
if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2, 'H': 8},
        'B': {'A': 4, 'C': 1, 'D': 5, 'E': 7},
        'C': {'A': 2, 'B': 1, 'D': 8, 'F': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6, 'G': 3},
        'E': {'B': 7, 'D': 2, 'G': 1},
        'F': {'C': 10, 'D': 6, 'G': 4, 'I': 9},
        'G': {'D': 3, 'E': 1, 'F': 4, 'I': 2, 'J': 7},
        'H': {'A': 8, 'I': 3},
        'I': {'F': 9, 'G': 2, 'H': 3, 'J': 5},
        'J': {'G': 7, 'I': 5}
    }

    start = 'A'
    nodes = dijkstra(graph, start=start)
    

    # Print shortest path to each node
    print(f"\nShortest paths from {start}:")
    for node_name, node in nodes.items():
        if node_name == start:
            print(f"  {start} -> {start}: ['{start}']")
            continue
            
        path = []
        current = node_name
        while current is not None:
            path.append(current)
            current = nodes[current].parent
        path.reverse()
        print(f"  {start} -> {node_name}: {path}")
