import random
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
matplotlib.use('TkAgg')
import scipy.stats as sts
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


data = pd.read_csv('insurance.csv')
print(data.describe())
print(data.info())

# data.hist()
# sns.displot(data['bmi'], kde=True)
# plt.show()

# Меры центральной тенденции
print('Медиана: %f' % np.median(data['bmi']))  # Элемент находящийся в середине отсортированной выборки
print('Мода: ', sts.mode(data['bmi']))  # Мода самое популярное значение
print('Среднее: %f' % np.mean(data['bmi']))
# Стоит отметить, что самой неустойчивой к выбросам мерой является среднее
# Cамой надежной или робастной является мода

# Меры изменчивости
print('Размах: %f' % (np.max(data['bmi']) - np.min(data['bmi'])))
print('Стандартное отклонение: %f' % np.std(data['bmi']))  # Корень из дисперсии
# Этот показатель позволяет оценить, как сильно меняются данные относительно их среднего
# Стандартное отклонение не устойчиво к выбросам
print('Межквартильный размах (np): %f' % (np.percentile(data['bmi'], 75, interpolation='midpoint') -
                                          np.percentile(data['bmi'], 25, interpolation='midpoint')))
print('Межквартильный размах (sts): %f' % sts.iqr(data['bmi'], interpolation='midpoint'))
# Это ширина интервала, который содержит 50% данных
# Эта метрика полезна для описания данных, она устойчива к выбросам

fig1 = plt.figure()
plt.vlines(x=np.median(data['bmi']), ymin=0, ymax=300, color='green')
plt.vlines(x=np.percentile(data['bmi'], 25, interpolation='midpoint'), ymin=0, ymax=300, color='yellowgreen')
plt.vlines(x=np.percentile(data['bmi'], 75, interpolation='midpoint'), ymin=0, ymax=300, color='darkgreen')
plt.hist(data['bmi'], color='lightgreen', bins=10)
green_patch = mpatches.Patch(color='green', label='Mean')
yellowgreen_patch = mpatches.Patch(color='yellowgreen', label='QR 25%')
darkgreen_patch = mpatches.Patch(color='darkgreen', label='QR 75%')
plt.legend(handles=[green_patch, yellowgreen_patch, darkgreen_patch])
# Интересная штука патчи
# plt.show()

fig2 = plt.figure()
plt.boxplot([data['age'], data['bmi'], data['children']], labels=['age', 'bmi', 'children'], vert=False)
plt.xticks(np.arange(0, 70, 5))

fig3 = plt.figure()
data.boxplot()

fig4 = plt.figure()
sns.boxplot(data=data)
# plt.show()

select = [random.sample(data, 300, counts=None), random.sample(data, 300, counts=None),
          random.sample(data, 300, counts=None), random.sample(data, 300, counts=None),
          random.sample(data, 300, counts=None), random.sample(data, 300, counts=None)]

