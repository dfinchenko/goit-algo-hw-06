import networkx as nx

def dfs(graph, start, goal):
    """Функція для пошуку шляху в графі методом DFS (пошук у глибину)."""
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, start, goal):
    """Функція для пошуку шляху в графі методом BFS (пошук у ширину)."""
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))


if __name__ == "__main__":
    # Ініціалізація графа
    G = nx.Graph()

    # Додавання вершин (станцій)
    stations = ["Станція 1", "Станція 2", "Станція 3", "Станція 4", "Станція 5"]
    G.add_nodes_from(stations)

    # Додавання ребер (маршрутів між станціями)
    routes = [("Станція 1", "Станція 2"), ("Станція 2", "Станція 3"), ("Станція 3", "Станція 4"), 
            ("Станція 4", "Станція 5"), ("Станція 5", "Станція 1"), ("Станція 2", "Станція 4")]
    G.add_edges_from(routes)

    # Застосування функцій DFS і BFS до графа
    dfs_path = dfs(G, "Станція 1", "Станція 5")
    bfs_path = bfs(G, "Станція 1", "Станція 5")

    print("\nDFS шлях:", dfs_path)
    print("BFS шлях:", bfs_path)
    print("\nУ цьому графі, між \"Станція 1\" та \"Станція 5\" існує пряме з\'єднання, тому найкоротший шлях є очевидним і однаковим для обох алгоритмів.")