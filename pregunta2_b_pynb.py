# -*- coding: utf-8 -*-
"""Copia de pregunta2 b.pynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WDhogr4UWI0HclnuQLSytn5DRrNWI5es
"""

from google.colab import drive
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Montar Google Drive
drive.mount('/content/drive')

# Ruta al archivo CSV
file_path = '/content/drive/MyDrive/Breast_Cancer.csv'

# Leer el dataset con el delimitador correcto
column_names = ['Age', 'Race', 'Marital Status', 'T Stage', 'N Stage', '6th Stage',
                'Differentiation', 'Grade', 'A Stage', 'Tumor Size',
                'Estrogen Status', 'Progesterone Status', 'Survival Months', 'Status']

# Cargamos los datos, omitiendo la fila incorrecta
data = pd.read_csv(file_path, delimiter=';', names=column_names, skiprows=1)

# Convierto  las columnas a numéricas
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
data['Tumor Size'] = pd.to_numeric(data['Tumor Size'], errors='coerce')
data['Survival Months'] = pd.to_numeric(data['Survival Months'], errors='coerce')

# Estadísticas descriptivas
selected_columns = ['Age', 'Tumor Size', 'Survival Months']

for col in selected_columns:
    print(f"\nEstadísticas de la columna {col}:")
    print(f"Media: {data[col].mean()}")
    print(f"Mediana: {data[col].median()}")
    print(f"Desviación estándar: {data[col].std()}")
    print(f"Rango: {data[col].max() - data[col].min()}")

# Graficar mapa de calor de correlaciones
data_selected = data[selected_columns]
correlation_matrix = data_selected.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor de Correlaciones entre Age, Tumor Size y Survival Months')
plt.show()

# Opcional: Gráfico de dispersión para visualizar relaciones
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Tumor Size', y='Survival Months', hue='Age', palette='viridis', alpha=0.6)
plt.title('Gráfico de Dispersión: Tumor Size vs Survival Months')
plt.xlabel('Tumor Size')
plt.ylabel('Survival Months')
plt.legend(title='Age', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()