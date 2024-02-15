import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('month', help='Enter month', type=str)
parser.add_argument('year', help='Enter year', type=str)
args = parser.parse_args()

month = args.month
year = args.year

if int(month) < 1 or int(month) > 12:
    print('Укажите существующий месяц')
    sys.exit()
if int(year) > 2024 or int(year) < 2008:
    print('Данные за эти года не могут существовать')
    sys.exit()
if int(month) < 10 and int(month) > 0 and '0' not in month:
    month = '0' + month

output_data = pd.read_excel(f'outcome_{month}.{year}.xlsx')

fig, ax = plt.subplots(constrained_layout=True)
date = [int(x.split()[0]) for x in output_data['Дата']]
output_data['День'] = date
sns.lineplot(
    data = output_data,
    x = 'День',
    y = 'Сумма',
    hue='Категория',
    ax=ax
)
ax.grid()
ax.legend()
plt.title(month+'.'+year)
plt.show()
