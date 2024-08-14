import csv
import matplotlib.pyplot as plt

def read_sales_data(file_path):
    sales_data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, fieldnames=['product_name', 'quantity', 'price', 'date'])
        for row in reader:
            row['quantity'] = int(row['quantity'])
            row['price'] = float(row['price'])
            sales_data.append(row)
    return sales_data

def total_sales_per_product(sales_data):
    total_sales = {}
    for sale in sales_data:
        product_name = sale['product_name']
        if product_name not in total_sales:
            total_sales[product_name] = 0
        total_sales[product_name] += sale['quantity'] * sale['price']
    return total_sales

def sales_over_time(sales_data):
    sales_by_date = {}
    for sale in sales_data:
        date = sale['date']
        if date not in sales_by_date:
            sales_by_date[date] = 0
        sales_by_date[date] += sale['quantity'] * sale['price']
    return sales_by_date

file_path = 'file.txt'

sales_data = read_sales_data(file_path)

total_sales = total_sales_per_product(sales_data)
max_revenue_product = max(total_sales, key=total_sales.get)
print(f"Продукт, принесший наибольшую выручку: {max_revenue_product}")

sales_by_date = sales_over_time(sales_data)
max_sales_date = max(sales_by_date, key=sales_by_date.get)
print(f"День с наибольшей суммой продаж: {max_sales_date}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(list(total_sales.keys()), list(total_sales.values()))
plt.xlabel('Продукт')
plt.ylabel('Общая сумма продаж')
plt.title('Общая сумма продаж по продуктам')

plt.subplot(1, 2, 2)
plt.plot(list(sales_by_date.keys()), list(sales_by_date.values()))
plt.xlabel('Дата')
plt.ylabel('Общая сумма продаж')
plt.title('Общая сумма продаж по дням')

plt.tight_layout()
plt.show()