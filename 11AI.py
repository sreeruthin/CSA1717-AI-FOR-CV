from collections import deque

def is_valid_assignment(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, graph, colors):
    if len(assignment) == len(graph):
        return assignment

    unassigned_nodes = [node for node in graph if node not in assignment]
    node = unassigned_nodes[0]

    for color in colors:
        if is_valid_assignment(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(assignment, graph, colors)
            if result:
                return result
            del assignment[node]

    return None

def map_coloring(graph, colors):
    return backtrack({}, graph, colors)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
assignment = map_coloring(graph, colors)
print(assignment)
