import csv
import statistics

# Leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}

with open('platzi/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']  # Asegurar que coincide con el CSV
        sales = int(row['sales'])  # Asegurar que coincide con el CSV
        monthly_sales[month] = sales

# Convertir valores de ventas a una lista
sales = list(monthly_sales.values())

# Imprimir resultados
print("Datos de ventas mensuales:", monthly_sales)

# Calcular el promedio de ventas
mean_sales = statistics.mean(sales)
print("Promedio de ventas:", mean_sales)

# Calcular la mediana
median_sales = statistics.median(sales)
print("Mediana de ventas:", median_sales)

# Calcular la moda
mode_sales = statistics.mode(sales)
print("Moda de ventas:", mode_sales)

# Calcular la desviación estándar
std_dev_sales = statistics.stdev(sales)
print("Desviación estándar de ventas:", std_dev_sales)

# Calcular el coeficiente de variación
var_coef_sales = statistics.variance(sales) / mean_sales ** 2
print("Coeficiente de variación de ventas:", var_coef_sales)

# Calcular el rango intercuartil
iqr_sales = statistics.quantiles(sales, n=4)[2] - statistics.quantiles(sales, n=4)[1]
print("Rango intercuartil de ventas:", iqr_sales)

# Calcular el percentil 95
percentile_95_sales = statistics.quantiles(sales, n=100)[95]
print("Percentil 95 de ventas:", percentile_95_sales)

#  Calcular la variaza
variance_sales = statistics.variance(sales)
print("Varianza de ventas:", variance_sales)

# Calcular el maximo y minimo
max_sales = max(sales)
min_sales = min(sales)
print("Maximo de ventas:", max_sales)
print("Minimo de ventas:", min_sales)

# Calcular el rango de ventas
range_sales = max(sales) - min(sales)
print("Rango de ventas:", range_sales)