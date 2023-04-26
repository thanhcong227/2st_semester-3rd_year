#   Đường đi trong mê cung: Tìm đường đi từ A đến B trong mê cung với các cạnh có trọng số không âm bằng phương pháp Tracking Back.

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

graph = {'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []}

print(find_path(graph, 'A', 'F'))
