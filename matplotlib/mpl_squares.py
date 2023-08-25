import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
#Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=24) #Заголовок
plt.xlabel("Value", fontsize=14) #Ось X
plt.ylabel("Square of Value", fontsize=14) #Ось Y
# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize=14)

plt.show()
