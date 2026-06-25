import pandas as pd
import matplotlib.pyplot as plt

data = [7, 14, 11, 17, 21, 15, 18, 20, 30, 15]
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
plt.hist(data, bins=[5, 10, 15, 20, 25, 30, 35], edgecolor='black', color='skyblue', alpha=0.8)

plt.title('Хистограма на трудовия стаж във фирмата', fontsize=14)
plt.xlabel('Трудов стаж (години)', fontsize=12)
plt.ylabel('Брой работници (Честота)', fontsize=12)
plt.xticks([5, 10, 15, 20, 25, 30, 35])
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()