import networkx as nx
import matplotlib.pyplot as plt
import random

# Алгоритм Дейкстри для знаходження найкоротших шляхів
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph.nodes()}
    previous_vertices = {vertex: None for vertex in graph.nodes()}
    shortest_paths[start] = 0
    vertices = list(graph.nodes())
    
    while vertices:
        current_vertex = min(vertices, key=lambda vertex: shortest_paths[vertex])
        vertices.remove(current_vertex)
        
        for neighbor in graph.neighbors(current_vertex):
            edge_weight = graph[current_vertex][neighbor]['weight']
            alternative_route = shortest_paths[current_vertex] + edge_weight
            
            if alternative_route < shortest_paths[neighbor]:
                shortest_paths[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex
    
    return shortest_paths, previous_vertices

if __name__ == "__main__":
    # Граф
    G = nx.Graph()
    stations = ["Станція 1", "Станція 2", "Станція 3", "Станція 4", "Станція 5"]
    routes = [("Станція 1", "Станція 2"), ("Станція 2", "Станція 3"), ("Станція 3", "Станція 4"), 
            ("Станція 4", "Станція 5"), ("Станція 5", "Станція 1"), ("Станція 2", "Станція 4")]
    G.add_nodes_from(stations)
    G.add_edges_from(routes)

    # Додавання ваг до ребер графа
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)

    # Візуалізація графа з вагами
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=2, font_size=15)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Модель транспортної мережі міста з вагами ребер")
    plt.show()

    # Знаходження найкоротших шляхів від "Станція 1" до всіх інших
    shortest_paths, previous_vertices = dijkstra(G, "Станція 1")

    # Результат
    print("Найкоротші шляхи від Станція 1 до всіх інших станцій:")
    for station, distance in shortest_paths.items():
        print(f"{station}: {distance}")