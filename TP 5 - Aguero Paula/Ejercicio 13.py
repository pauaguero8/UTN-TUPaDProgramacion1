# 13) Dada la siguiente lista de puntajes de un videojuego:
# ● Mayor y menor.
# ● Ranking.
# ● Posición de 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print("Mayor:", max(puntajes))
print("Menor:", min(puntajes))

ranking = sorted(puntajes, reverse=True)

print("Ranking:")
for p in ranking:
    print(p)

for i in range(len(ranking)):
    if ranking[i] == 990:
        print("Posición de 990:", i + 1)