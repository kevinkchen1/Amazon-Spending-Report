import pandas as pd
import matplotlib.pyplot as plt
info = pd.read_csv('reports.csv')
info = info.fillna(0)
info['Total Charged'] = info['Total Charged'].str.replace('$','').astype(float)
total = info['Total Charged'].sum()
print('Total spending:', total)
avg = info['Total Charged'].mean()
print('Average order cost:', avg)
max = info['Total Charged'].max()
print('Highest purchase cost:', max)
min = info['Total Charged'].min()
print('Lowest purchase cost:', min)
info['Order Date'] = pd.to_datetime(info['Order Date'])
indv_order = info.groupby('Order Date').sum()['Total Charged']
indv_order.plt.bar()
