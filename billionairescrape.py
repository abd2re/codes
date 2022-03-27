import pandas as pd
import numpy as np
excel_path = 'testt.xlsx'
src = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'

b_list = pd.read_html(src)[2]
b_list.set_index('No.',inplace=True)

net_worth = []
for n in b_list['Net worth (USD)']:
    n = ''.join(i for i in n if i.isdigit() or i in '-.')
    net_worth.append(float(n))


b_list.insert(2,'num',net_worth)

dataset = [
    b_list.drop('num',axis=1),
    b_list.groupby('Nationality').count().loc[:,'num'].sort_values(ascending=False).reset_index().set_axis(['countries','count'], axis=1),
    b_list.groupby('Nationality').sum().loc[:,'num'].sort_values(ascending=False).reset_index().set_axis(['countries','sum'], axis=1),
    b_list.groupby('Nationality').mean().loc[:,'num'].sort_values(ascending=False).reset_index().set_axis(['countries','mean'], axis=1),
    b_list.groupby('Nationality').max().loc[:,'num'].sort_values(ascending=False).reset_index().set_axis(['countries','max'], axis=1)
]

pd.concat(dataset,axis=1).fillna('').to_excel('billionaire_sheet.xlsx')
