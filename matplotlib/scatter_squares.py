import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# edgecolor - цвет контура точек. color(c) - цвет точек (Поддерживает RGB)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)
# cmap(colormap) - градиент от начального цвета к конечному

# Назначение заголовка диаграммы и меток осей
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона для каждой оси.
plt.axis([0, 1100, 0, 1100000])

""" Сохранение диаграммы в файле.
    1 арг. - имя. 
    2 арг. - отсекает от диаграммы лишние пропуски """
plt.savefig('squares_plot.png', bbox_inches='tight')
"""Для вывода диаграммы на экран plt.show()"""
