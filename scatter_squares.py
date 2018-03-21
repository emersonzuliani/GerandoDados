import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

print(y_values)

#c=(R, G, B) --> escala de 0 a 1 para cada cor.
#edgecolor --> cor da borda. 'none' para retirar a borda
#s --> tamanho do ponto no Scatter

#plt.scatter(x_values, y_values, c=(0, 0, 1), edgecolor='none', s=4)

#usando colormap
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=10)

#definir o título do gráfico e eixos
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()

#para salvar a figura automaticamente, omitir o plt.show() e chamar o savefig
#plt.savefig('squares_plot.png', bbox_inches='tight')
