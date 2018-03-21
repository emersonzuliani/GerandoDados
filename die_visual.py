#die_visual.py
import pygal
from die import Die

#cria um D6
die = Die()

#Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print('Frenquencias: {}'.format(frequencies))

#Visualiza os resultados
hist = pygal.Bar()

hist.title = 'Resultados de um D6 1000 vezes'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
