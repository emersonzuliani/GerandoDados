import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5]
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

print(y_values)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolor='none', s=10)

#definir titulo e eixos
plt.title('Cubos', fontsize=20)
plt.xlabel('Values', fontsize=14)
plt.ylabel('Cubos', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=14)



plt.show()
