import heapq

class Node:
    def __init__(self, name, g, h, parent=None):
        self.name = name
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def a_star(graph, start, goal, h):
    open_list = []
    closed_list = set()
    start_node = Node(start, 0, h[start])
    heapq.heappush(open_list, start_node)
    came_from = {}

    while open_list:
        current = heapq.heappop(open_list)

        if current.name == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1], current.g

        closed_list.add(current.name)

        for neighbor, cost in graph[current.name].items():
            if neighbor in closed_list:
                continue

            g_score = current.g + cost
            h_score = h[neighbor]
            neighbor_node = Node(neighbor, g_score, h_score, current)

            if not any(node.name == neighbor and node.f <= neighbor_node.f for node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None, float('inf')

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

path, cost = a_star(graph, 'A', 'D', h)
print(f"Path: {path}, Cost: {cost}")
