#rw_visual.py
import matplotlib.pyplot as plt
from random_walk import RandomWalk


#Cria um passeio aleatório a plota os pontos

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.figure(dpi=128, figsize=(10, 6))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.get_cmap('Blues'), edgecolor='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    #remove os eixos
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Construir outro passeio? (s/n): ')
    if keep_running == 'n':
        break

