import pandas as pd
import scipy.stats as sts

data = pd.read_csv('MeteorLandClean.csv', delimiter=',')
data.drop('hui', axis=1, inplace=True)
print(data)

print('Меры центральной тенденции:', '\n')
print('Среднее: %.3f' % data['mass (g)'].mean())
print('Медиана: %.3f' % data['mass (g)'].median())
print('Мода: ', sts.mode(data['mass (g)']), '\n')

print('Меры изменчивости:', '\n')
print('Размах: %.3f' % (data['mass (g)'].max() - data['mass (g)'].min()))
print('Среднеквадратическое отклонение(для выборки: стандартное): %.3f' % data['mass (g)'].std())
print('Межквартильный размах: ', sts.mode(data['mass (g)']), '\n')

print('Сводка о числовых данных таблицы (count, mean, std, min, %, max)', '\n',
      data.describe(), '\n')
