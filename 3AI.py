from collections import deque

def bfs(capacity_a, capacity_b, target):
    queue = deque()
    visited = set()
    
    queue.append((0, 0))
    visited.add((0, 0))
    
    while queue:
        current_a, current_b = queue.popleft()
        
        if current_a == target or current_b == target:
            print(f"Solution found: Jug A = {current_a}, Jug B = {current_b}")
            return True
        
        possible_actions = [
            (capacity_a, current_b),
            (current_a, capacity_b),
            (0, current_b),
            (current_a, 0),
            (current_a - min(current_a, capacity_b - current_b), current_b + min(current_a, capacity_b - current_b)),
            (current_a + min(current_b, capacity_a - current_a), current_b - min(current_b, capacity_a - current_a)),
        ]
        
        for next_a, next_b in possible_actions:
            if (next_a, next_b) not in visited:
                visited.add((next_a, next_b))
                queue.append((next_a, next_b))
    
    print("No solution found.")
    return False

capacity_a = 4
capacity_b = 3
target = 2

bfs(capacity_a, capacity_b, target)
