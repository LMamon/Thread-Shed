import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

def totalSales(Sales):    #calculate total sales
    profit = 0
    for sale in Sales:
        profit += float(sale.strip('$'))
    return f'Total sales: \n\t ${profit:.2f}'

def threadsSold(Colors):    #how many threads sold of each color
    for color in Colors:
        if "&" in color:
            Threads_sold.extend(color.split('&'))
        else:
            Threads_sold.append(color)
    return Threads_sold

color_counts = pd.Series(Threads_sold).value_counts()
print(color_counts)

def colorCount(color):    #calculate number of each color sold
    return sum(1 for item in Threads_sold if color.lower() == item.lower())

def printColorsSold(Threads_sold):
    color_list=[]
    for color in Threads_sold:
        if color.capitalize() not in color_list:
            color_list.append(color.capitalize())
    
    print(f'Colors sold:\n\t{color_list}')
    for item in color_list:     #print number of threads sold for each color
        print(f'Sold {colorCount(item)} {item} today')

Thread_List = threadsSold(Sold_Colors)
printColorsSold(Thread_List)


def QtyXColor():
    df = pd.read_csv('clean_sales.csv')
    color_counts = df['Color'].value_counts()

    fig, ax =plt.subplots()
    ax.bar(color_counts.index, color_counts.values)
    
    for i, count in enumerate(color_counts.values):
        plt.text(i, count, str(count))
    plt.xticks(rotation=0)
    plt.show()
    main()
    

def expensiveColor():
    df = pd.read_csv('clean_sales.csv') #load

    color_profits = df.groupby('Color')['Sale_Price'].sum() #group by color and sum sales

    fig, ax= plt.subplots()
    ax.plot(color_profits.index, 
               color_profits.values, 
               color= 'green',
               drawstyle = 'default')
    plt.show()
    main()

def heatMap():
    df = pd.read_csv('clean_sales.csv') #load

    #create pivot table
    pivot = df.pivot_table(index='Customer',
                           columns='Color',
                           values='Sale_Price',
                           aggfunc='sum',
                           fill_value=0)

    #createheatmap
    sns.heatmap(pivot, annot= False,
                cmap='plasma')
    
    plt.show()
    main()

def exportToCSV(): #move extracted data from .txt into a new csv
    export = pd.DataFrame({'Customer' : Customer,
                          'Sale_Price' : Sales,
                          'Color' : Thread_List[:100],
                          'Date' : Date})
    
    export.to_csv('clean_sales.csv', index=False)
    main()

def main():
    print("\t\tprompt head")
    print(totalSales(Sales))
    choice = input("""\nQty by color bar graph(1)
                   \nSales over time(2)
                   \nheat map of sales by color over time(3)
                   \nexport(4)
                   \nExit(q)\n""")
    
    options = {
        '1' : QtyXColor,
        '2' : expensiveColor,
        '3' : heatMap,
        '4' : exportToCSV,
        'q' : sys.exit
    }

    while choice not in options:
        choice = input("Please enter valid option")
    options[choice]()

main()
    