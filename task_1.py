import networkx as nx
import matplotlib.pyplot as plt

# Ініціалізація графа
G = nx.Graph()

# Додавання вершин (станцій)
stations = ["Станція 1", "Станція 2", "Станція 3", "Станція 4", "Станція 5"]
G.add_nodes_from(stations)

# Додавання ребер (маршрутів між станціями)
routes = [("Станція 1", "Станція 2"), ("Станція 2", "Станція 3"), ("Станція 3", "Станція 4"), 
          ("Станція 4", "Станція 5"), ("Станція 5", "Станція 1"), ("Станція 2", "Станція 4")]
G.add_edges_from(routes)

# Візуалізація графа
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=2, font_size=15)
plt.title("Модель транспортної мережі міста")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_nodes = G.degree()


report = f"Загальна інформація про граф:\n" \
         f"- Кількість вершин (станцій): {num_nodes}\n" \
         f"- Кількість ребер (маршрутів): {num_edges}\n\n" \
         f"Ступінь кожної вершини:\n"

for station, degree in degree_of_nodes:
    report += f"- {station}: {degree} з'єднань\n"

print(report)