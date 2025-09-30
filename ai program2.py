from collections import deque
def water_jug(a, b, target):
    visited = set()
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(x, y)
        if x == target or y == target:
            return
        q.extend([
            (a, y), (x, b), (0, y), (x, 0),
            (x - min(x, b - y), y + min(x, b - y)),
            (x + min(y, a - x), y - min(y, a - x))
        ])

water_jug(4, 3, 2)
