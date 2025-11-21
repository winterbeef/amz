#!/usr/bin/env python3

from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])

    while queue:
        cur = queue.popleft()
        print(f"Visiting: {cur}")

        node = graph[cur]
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"Added to queue: {neighbor}")

# Return a dict of nodes by name
def make_nodes(graph):
    result = {}
    for name, neighbors in graph.items():
        cur_node = result.get(name, Node(name))

        for neighbor in neighbors:
            neighbor_node = result.get(neighbor, Node(neighbor))
            cur_node.neighbors[neighbor] = neighbor_node

        result[name] = cur_node
    return result

def print_nodes(nodes):
    for name,node in nodes.items():
        print('=======')
        print(f"name: {name}")
        print(f"neighbors: {list(node.neighbors.keys())}")


# Example Usage.
# Reusing a graph with weights.
# Ignore weights for simple BFS
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

    foo = make_nodes(graph=graph)
    # print_nodes(foo)

    bfs(foo, 'G')
