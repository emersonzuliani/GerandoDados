#random_walk
from random import choice

class RandomWalk():
    """Uma classe para gerar passeios aleatórios"""

    def __init__(self, num_points=5000):
        """Inicia os atributos de um passeio"""
        self.num_points = num_points

        #Todos os passeios começam em (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todos os pontos do passesio"""

        #Continua dando passos até que o passeio alcance o tamanho desejado
        while len(self.x_values) < self.num_points:
            #decide direção a ser seguida e distÂncia a ser percorrida nessa direção
            x_step = self.get_step()
            y_step = self.get_step()

            #rejeita movimentos que não vão a lugar nenhum
            if x_step == 0 and y_step == 0:
                continue

            #calcula os próximos valores de x e de y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([1, 2, 3, 4, 5])
        step = direction * distance
        return step
