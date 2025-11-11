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
        self.is_explored = True

def dijkstra(graph, start):
    # node.dist == best from origin
    # graph[from][to] == edge distance

    nodes = {n:Node() for n in graph}
    nodes[start].newbest(parent=None, dist=0)

    minheap = heapq.heapify([(nodes[start].dist, start)])

    while minheap:
        curdist, cur = heapq.heappop(minheap)
        nodes[cur].is_explored = True

        for child, edge in graph[cur].items():
            if nodes[child].is_explored:
                continue

            newdist = curdist + edge
            if newdist < nodes[child].dist:
                nodes[child].newbest(parent=cur, dist=newdist)
                heapq.heappush( (newdist, child) )

# Example Usage:
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start = 'A'
    results = dijkstra(graph, start=start)
