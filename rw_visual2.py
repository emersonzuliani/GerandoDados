#rw_visual2.py
import matplotlib.pyplot as plt
from random_walk import RandomWalk


#Cria um passeio aleatório a plota os pontos

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(rw.x_values, rw.y_values, linewidth=2)
    #plt.plot(rw.x_values, rw.y_values, edgecolor='none', linewidth=10)

    #remove os eixos
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Construir outro passeio? (s/n): ')
    if keep_running == 'n':
        break
