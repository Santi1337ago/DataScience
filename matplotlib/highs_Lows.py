import csv

from matplotlib import pyplot as plt

from datetime import datetime

# Разбор заголовка файла CSV
filename = 'death_valley_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Печать заголовков и их позиций
    """for index, column_header in enumerate(header_row):
        print(index, column_header)"""
    # Извлечение и чтение данных
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            low = int(row[4])
            high = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        finally:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1) # закрашиваем область

# Форматирование диаграммы.
plt.title('Daily high temperatures, Jule 2021\nDeath Valley, CA', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
