import pandas as pd
import matplotlib.pyplot as plt

filename = r'C:/Users/chira/Documents/retail.csv'

df = pd.read_csv(filename)
df['Order_Date']=pd.to_datetime(df['Order_Date'])

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
AOV = (total_sales/df['Sales'].count())
pm = (total_profit/total_sales)*100

cat_sales_region=df.pivot_table(values=['Sales','Profit'],index='Category',columns='Region',aggfunc='sum')
cat_sales_region.plot(kind='bar')
plt.title('Sales and profit By Category and Region')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.legend(title='Region')
plt.show()

sub_sales_region=df.pivot_table(values=['Sales','Profit'],index='Sub_Category',columns='Region',aggfunc='sum')
sub_sales_region=sub_sales_region.fillna(0)
sub_sales_region.plot(kind='bar')
plt.title('Sales and profit By Sub-Category and Region')
plt.xlabel('Sub_Category')
plt.ylabel('Sales')
plt.legend(title='Region')
plt.show()

Profit_Margin =((cat_sales_region['Profit']/cat_sales_region['Sales'])*100).round()
Profit_Margin.plot(kind='bar')
plt.title('Profit Margin By Category and Region')
plt.xlabel('Category')
plt.ylabel('Profit Margin')
plt.show()

df['Month']=df['Order_Date'].dt.to_period('M')
monthly = df.groupby('Month')[['Sales','Profit']].sum()
monthly.plot(kind='line',marker=0)
plt.title('Monthly Trend of Sales and Profit')
plt.legend(title='metrics')
plt.show()

print('SALES AND PROFIT BY CATEGORY AND REGION')
print(cat_sales_region)
print()
print('SALES AND PROFIT BY SUB-CATEGORY AND REGION')
print(sub_sales_region)
print()
print('PROFIT MARGIN BY CATEGORY AND REGION')
print(Profit_Margin)
print()
print('Total Sales:',total_sales)
print()
print('Total_Profit:',total_profit)
print()
print('Profit Margin:',pm.round())
print()
print('AOV:',AOV.round())
print()
print(monthly)
