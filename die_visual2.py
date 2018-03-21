#die_visual.py
import pygal
from die import Die

def lanca_dado(die, times):
    results = []
    for roll_num in range(times):
        result = die.roll()
        results.append(result)
    return results

def sum_frequencies(results, max_result):
    frequencies = []
    for value in range(1, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)
    return frequencies


#cria um D6
die_1 = Die()
die_2 = Die()

#Faz alguns lançamentos e armazena os resultados em uma lista
res_die1 = lanca_dado(die_1, 1000)
res_die2 = lanca_dado(die_2, 1000)

print(res_die1)
print(res_die2)

frequencies_1 = sum_frequencies(res_die1, 6)
frequencies_2 = sum_frequencies(res_die2, 6)

print('Frenquencias: {}'.format(frequencies_1))
print('Frenquencias: {}'.format(frequencies_2))

x_label = list(range(1, 7))


#Visualiza os resultados
hist = pygal.Bar()

hist.title = 'Resultados de um D6 1000 vezes'
hist.x_labels = x_label
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 1', frequencies_1)
hist.add('D6 2', frequencies_2)
hist.render_to_file('die_visual2.svg')
print('Arquivo die_visual2.svg criado!')

