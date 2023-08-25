import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму.
rw = RandomWalk(50000)
rw.fill_walk()
# Назначение размера области просмотра.
plt.figure(dpi=512, figsize=(10, 6))
plt.scatter(rw.x_values, rw.y_values, s=15)
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
# Выделение первой и последней точек.
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
"""Удаление осей"""
# get current axes
ax = plt.gca()
# hide x-axis
ax.get_xaxis().set_visible(False)
# hide y-axis
ax.get_yaxis().set_visible(False)
plt.savefig('rw.png', bbox_inches='tight')
