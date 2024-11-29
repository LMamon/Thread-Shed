
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt



#read & clean data
with open('daily_sales.txt', 'r' ) as f:
    raw_data = f.read().replace(';,;', ',').split(sep=',')


#create lists
Customer, Sales, Sold_Colors, Date, Threads_sold = [], [], [], [], []

for sale in range(0, len(raw_data), 4):
    Customer.append(raw_data[sale].strip())
    Sales.append(raw_data[sale + 1].strip())
    Sold_Colors.append(raw_data[sale + 2].strip())
    Date.append(raw_data[sale + 3].strip())


#calculate total sales
total_sales = 0

for sale in Sales:
    total_sales += float(sale.strip('$'))

print(f'Total sales: \n\t ${total_sales:.2f}')

#how many threads sold of each color
for color in Sold_Colors:
    if "&" in color:
        Threads_sold.extend(color.split('&'))
    else:
        Threads_sold.append(color)

def color_count(color):
    return sum(1 for item in Threads_sold if color.lower() == item.lower())

#could go through sold color and add any color not already in the list
color_list=[]
for color in Threads_sold:
    if color.capitalize() not in color_list:
        color_list.append(color.capitalize())

print(f'Colors sold:\n\t{color_list}')

#print number of threads sold for each color

for item in color_list:
    print(f'Sold {color_count(item)} {item} today')



