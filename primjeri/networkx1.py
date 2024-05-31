import networkx as nx
import matplotlib.pyplot as plt

# Definisemo matricu susjedstva (redovi su cvorovi, kolone su kapaciteti grana)
matrica = [[0, 16, 13, 0, 0, 0],
    [0, 0, 0, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]]

# Kreiramo usmjereni graf
G = nx.DiGraph()

# U graf dodajemo grane iz matrice susjedstva
for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        if matrica[i][j] != 0:
            G.add_edge(i, j, capacity=matrica[i][j])

# Racunamo maksimalni protok
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
