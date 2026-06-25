import pandas as pd
import matplotlib.pyplot as plt

data = [7, 14, 11, 17, 17, 21, 15, 15,
18, 11, 15, 16, 20, 14, 25, 25, 35, 27, 24, 24, 31, 28, 33, 25, 28, 33, 24, 7, 13, 21, 16, 22,
23, 28, 23, 27, 27, 31, 34, 34, 37, 41, 20, 41, 13, 20, 20, 25, 30, 22, 22, 34, 31, 34, 24, 29,
34, 36, 8, 37]
n = len(data)
print(f"Обем на извадката (n): {n}\n")

sorted_data = sorted(data)
print(f"Вариационен ред: {sorted_data}\n")

series_data = pd.Series(sorted_data)

freq_table = series_data.value_counts().sort_index().reset_index()
freq_table.columns = ['Стаж (x)', 'Честота (m)']

freq_table['Кумулативна честота'] = freq_table['Честота (m)'].cumsum()

print("Таблица на разпределението:")
print(freq_table.to_string(index=False))

plt.figure(figsize=(8, 5))
plt.hist(data, bins=[5, 10, 15, 20, 25, 30, 35, 40, 45], edgecolor='black', color='skyblue', alpha=0.8)

plt.title('Хистограма на трудовия стаж във фирмата', fontsize=14)
plt.xlabel('Трудов стаж (години)', fontsize=12)
plt.ylabel('Брой работници (Честота)', fontsize=12)
plt.xticks([5, 10, 15, 20, 25, 30, 35, 40, 45])
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()