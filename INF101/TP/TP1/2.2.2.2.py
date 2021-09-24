import random
import matplotlib.pyplot as plt
import time
from collections import Counter, OrderedDict
import multiprocessing as mp

fois_jouer = int(input("Combien de fois tu vous jouer?"))
nombre_fois_utilise_total = 0
nombre_maximeme = 99
fois_count = []
start_time = time.time()

for i in range(0, fois_jouer):
    nombre_random = random.randint(0, nombre_maximeme)
    print("Le nombre correst est %s" % nombre_random)
    nombre_temp_gauche = 0
    nombre_temp_droite = nombre_maximeme
    nombre_fois_utilise_une_fois = 0
    while True:
        nombre_temp_random = random.randint(nombre_temp_gauche, nombre_temp_droite)
        print("Je choisi %s (%s fois)" % (nombre_temp_random, nombre_fois_utilise_une_fois + 1))
        if nombre_temp_random < nombre_random:
            print("Cest trop petit")
            nombre_fois_utilise_une_fois += 1
            nombre_temp_gauche = nombre_temp_random + 1
            print("Je vais essayer %s a %s\n" % (nombre_temp_gauche, nombre_temp_droite))
        elif nombre_temp_random > nombre_random:
            print("Cest trop grand")
            nombre_fois_utilise_une_fois += 1
            nombre_temp_droite = nombre_temp_random - 1
            print("Je vais essayer %s a %s\n" % (nombre_temp_gauche, nombre_temp_droite))
        else:
            print("Yea, le bon reponse est: %s" % nombre_temp_random)
            nombre_fois_utilise_une_fois += 1
            nombre_fois_utilise_total += nombre_fois_utilise_une_fois
            print("---------------------------------")
            fois_count.append(nombre_fois_utilise_une_fois)
            break

print("Il utilise %s fois en %s jeu(s).\nEn moyenne il utilise %s fois chaque jeu" % (
    nombre_fois_utilise_total, fois_jouer, nombre_fois_utilise_total / fois_jouer))
print(fois_count)
print(time.time() - start_time, "seconds")

plt.subplot(211)
plt.plot(fois_count, "ro")
plt.plot(fois_count)

plt.subplot(212)
count = Counter(fois_count)
print(count)
plt.bar(count.keys(), count.values())
plt.xlabel("Fois Utilise")
plt.ylabel("Fois Count")
plt.grid(True)

for i in (count.keys()):
    v = count.get(i)
    plt.text(i, v + 5, "%d" % v, ha="center")
plt.show()
