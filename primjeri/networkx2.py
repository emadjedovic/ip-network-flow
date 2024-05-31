import networkx as nx
import matplotlib.pyplot as plt

matrica = [
    [0, 10, 0, 8, 0, 0],
    [0, 0, 5, 2, 0, 0],
    [0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 10, 0],
    [0, 0, 8, 0, 0, 10],
    [0, 0, 0, 0, 0, 0]
]

G = nx.DiGraph()

for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        if matrica[i][j] != 0:
            G.add_edge(i, j, capacity=matrica[i][j])

maks_protok, mapa_protoka = nx.maximum_flow(G, 0, 5)

print("\nMaksimalni protok: ", maks_protok)
print("\nProtok kroz grane:")
for u in mapa_protoka:
    for v in mapa_protoka[u]:
        print(f"Grana ({u}, {v}): {mapa_protoka[u][v]}")
print()

# Vizualizacija

plt.figure(figsize=(10, 6))

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12)

oznake_grana = {(u, v): f"{mapa_protoka[u][v]}/{G[u][v]['capacity']}" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=oznake_grana)

plt.title("Maksimalni protok sa NetworkX i Matplotlib")
plt.show()
