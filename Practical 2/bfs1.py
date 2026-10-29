from collections import deque

# Graph representation
graph = {
    5: [3,7],
    3:[2,4],
    7: [8],
    2: [],
    4:[8],
    8:[],
}

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

bfs(5)