from collections import deque


class WeightedGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = []  # список (сосед, вес)

    def add_edge(self, from_node, to_node, weight):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].append((to_node, weight))


# обход в глубину
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    print(start_node, end=" ")
    for neighbor, weight in graph.nodes[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# обход в ширину
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor, weight in graph.nodes[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Создание графа
weight_graph_test = WeightedGraph()

for i in range(1, 11):
    weight_graph_test.add_node(i)

weighted_edges = [
    (1, 2, 5), (1, 3, 3), (1, 4, 7),
    (2, 5, 4), (2, 6, 6),
    (3, 5, 2), (3, 7, 8),
    (4, 8, 5), (4, 9, 4),
    (5, 10, 3), (6, 10, 7),
    (7, 10, 4), (8, 10, 6),
    (9, 10, 5),
    (5, 2, 4), (10, 5, 3)
]

for from_node, to_node, weight in weighted_edges:
    weight_graph_test.add_edge(from_node, to_node, weight)

# Вывод графа
for node in weight_graph_test.nodes:
    print(f"{node} -> {weight_graph_test.nodes[node]}")

print("Обход в глубину:")
dfs(weight_graph_test, 1)
print()

print("Обход в ширину:")
bfs(weight_graph_test, 1)
