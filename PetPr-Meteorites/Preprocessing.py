import random
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
matplotlib.use('TkAgg')
import scipy.stats as sts
import matplotlib.pyplot as plt


data = pd.read_csv('MeteoriteLandings.csv', delimiter=',')

print('Выводит все данные:', '\n',
      data, '\n')
print('По умолчанию выводит первые 5 строк:', '\n',
      data.head(7))
print('Информация о количестве, типе, заполненности данных по столбцам, кол-ве занимаемой памяти:', '\n',
      data.info(), '\n')
print('Вывод количества нулевых значений:', '\n',
      data.isna().sum(), '\n')
print('Выводит True, если строка дублируется, use without unique:', '\n',
      data.duplicated().unique(), '\n')
print('Проверка, что нет опечаток и данные корректны:', '\n',
      data.nametype.unique(), '\n')

sns.heatmap(data.head(100).isna(), cmap=sns.color_palette(['green', 'white']))  # удобно использовать при небольшом
# кол-ве строк

plt.figure()
plt.bar(data.keys(), data.isna().sum())  # количество пропусков по признакам - визуализация
plt.xticks(rotation=90)

print('Процентное содержание пропусков: ', '\n')
for column in data.columns:
    per = np.mean(data[column].isna() * 100)
    print(column, ' %.1f' % per)
print('\n')
data['mass (g)'].fillna(data['mass (g)'].mean(), inplace=True)
data.year.fillna(sts.mode(data.year)[0], inplace=True)
data.dropna(subset='reclat', inplace=True)

dataKeys = ['mass (g)', 'id', 'year', 'reclat', 'reclong']
fig, ims = plt.subplots(1, 5)
for i, x in enumerate(dataKeys, start=0):
    ims[i].boxplot(data[x])  # ничего не выводит, если есть нулевые значения в столбце
    ims[i].set_title(x)

plt.figure()
plt.boxplot(data['mass (g)'], vert=True)
arraySize = data.shape[0]
randomArray = [random.uniform(0, 2) for _ in range(arraySize)]
plt.scatter(randomArray, data['mass (g)'], s=1.5)
#plt.show()

data.fall.replace({'Fell': 0, 'Found': 1}, inplace=True)
data.drop('nametype', axis=1, inplace=True)
data.drop('GeoLocation', axis=1, inplace=True)

# !!!! Выполнять лишь раз
fileSave = open('D:\PycharmProjects\BigData\PetPr-Meteorites\MeteorLandClean.csv', 'w')
fileSave.close()
data.to_csv('MeteorLandClean.csv')
# !!!!
