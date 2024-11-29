import pandas as pd
import numpy as np


daily_sales_replaced = daily_sales.replace(';,;', '_')
print(daily_sales_replaced)
daily_transactions = daily_sales_replaced.split(',')
daily_transactions_split = []
for trans in daily_transactions:
    daily_transactions_split.append(trans.split('_'))
print(daily_transactions_split)

transactions_clean = []
for trans in daily_transactions_split:
    for data in trans:
        transactions_clean.append(data.strip())

customers, sales, threads_sold = [], [], []
print(transactions_clean)
for item in range(0, len(transactions_clean), 4):
    customers.append(transactions_clean[item])
    sales.append(transactions_clean[item +1])
    threads_sold.append(transactions_clean[item+2])
    
print()
print(customers)
print()
print(sales)
print()
print(threads_sold)
print()

total_sales = 0
for sale in sales:
    total_sales += float(sale.strip('$'))

print()
print('%.2f' %total_sales)

threads_sold_split = []
for color in threads_sold:
    if "&" in color:
        threads_sold_split.extend(color.split('&'))
    else:
        threads_sold_split.append(color)

def color_count(color):
    return sum(1 for item in threads_sold_split if color in item)

print(color_count('white'))

colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']
print()
for item in colors:
    script = "{} {} threads sold today."
    print(script.format(color_count(item), item))