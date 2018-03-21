#die_visual.py
import pygal
from die import Die

#cria um D6
die_1 = Die()
die_2 = Die()

#Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print('Frenquencias: {}'.format(frequencies))

x_label = list(range(2, max_result + 1))
print(x_label)

#Visualiza os resultados
hist = pygal.Bar()

hist.title = 'Resultados de um D6 1000 vezes'
hist.x_labels = x_label
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
print('Arquivo dice_visual.svg criado!')
