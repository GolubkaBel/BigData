import math
import pandas as pd
import numpy as np
import scipy.stats as sts
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

data = pd.read_csv('insurance.csv')
#print(data.describe())
dictSex = {'female': 1, 'male': 0}
dictSmoker = {'yes': 1, 'no': 0}
d = {'sex': dictSex, 'smoker': dictSmoker}
for row, dictRow in d.items():
    for oldValue, newValue in dictRow.items():
        data[row] = data[row].replace(oldValue, newValue)
#print(data.head())

#data.hist()
fig1, im = plt.subplots(1, 6)
im[0].hist(data['age'], bins=15)
im[0].set_title('age')
im[1].hist(data['sex'], bins=2)
im[1].set_title('sex')
im[2].hist(data['bmi'], bins=45)
im[2].set_title('bmi')
im[3].hist(data['children'], bins=3)
im[3].set_title('children')
im[4].hist(data['smoker'], bins=2)
im[4].set_title('smoker')
im[5].hist(data['charges'], bins=45)
im[5].set_title('charges')
plt.show()

meanBmi = np.mean(data['bmi'])
modaBmi = sts.mode(data['bmi'])
medBmi = np.median(data['bmi'])
meanCharges = np.mean(data['charges'])
modaCharges = sts.mode(data['charges'])
medCharges = np.median(data['charges'])
print('Mean(bmi, charges) = %f, %d' %(meanBmi, meanCharges))
print('Moda(bmi, charges) = ',modaBmi, ',\n     ', modaCharges)
print('Med(bmi, charges) = %f, %f'%(medBmi, medCharges))
fig2, im2 = plt.subplots(1, 2)
im2[0].hist(data['bmi'])
im2[0].vlines(x=[meanBmi], ymin=0, ymax=320, color='red')
im2[0].vlines(x=[modaBmi[0]], ymin=0, ymax=320, color='yellow')
im2[0].vlines(x=[medBmi], ymin=0, ymax=320, color='green')
red_patch = mpatches.Patch(color='red', label='Mean')
yellow_patch = mpatches.Patch(color='yellow', label='Mode')
green_patch = mpatches.Patch(color='green', label='Median')
im2[0].legend(handles=[red_patch, yellow_patch, green_patch])
im2[1].hist(data['charges'])
im2[1].vlines(x=[meanCharges], ymin=0, ymax=320, color='red')
im2[1].vlines(x=[modaCharges[0]], ymin=0, ymax=320, color='yellow')
im2[1].vlines(x=[medCharges], ymin=0, ymax=320, color='green')
im2[1].legend(handles=[red_patch, yellow_patch, green_patch])

d = ['age', 'bmi', 'children', 'charges']
fig3, im3 = plt.subplots(1, 4)
for i, x in enumerate(d, start=0):
    im3[i].boxplot(data[x])
    im3[i].set_title(x)

fig4 = plt.figure()
ds = data.sample(300)['bmi']
ax = ds.hist(bins=20, density=True)
xs = sorted(ds)
df = pd.DataFrame()
df[0] = xs
df[1] = sts.norm.pdf(xs, data['bmi'].mean(), data['bmi'].std())
df.plot(0, 1, linewidth=2, color='r', legend=None, ax=ax)
plt.axvline(x = data['bmi'].mean(), color='g')
plt.axvline(x = data['bmi'].mean()-np.std(data['bmi']), color='r')
plt.axvline(x = data['bmi'].mean()+np.std(data['bmi']), color='r')
print('Среднее отклонение: ', np.std(data['bmi']))

ds = data.sample(300)['charges']
dataSorted = sorted(ds)
df = pd.DataFrame()
df[0] = dataSorted
df[1] = sts.norm.pdf(dataSorted, data['charges'].mean(), data['charges'].std())
df.plot(0, 1, linewidth=2, color='g', label=None)
se = ds.std()/math.sqrt(len(ds))
tBorder95 = ds.mean() + 1.96*se
bBorder95 = ds.mean() - 1.96*se
tBorder99 = ds.mean() + 2.58*se
bBorder99 = ds.mean() - 2.58*se
plt.axvline(x = tBorder95, color = 'b', label = 'tBorder95')
plt.axvline(x = bBorder95, color = 'b', label = 'bBorder95')
plt.axvline(x = tBorder99, color = 'r', label = 'tBorder99')
plt.axvline(x = bBorder99, color = 'r', label = 'bBorder99')
plt.axvline(x = data['charges'].mean(), color = 'g', label = 'mean')
plt.legend()

# g = sns.jointplot(x=sorted(data['bmi']),
 #                  y=sts.norm.pdf(sorted(data['bmi']), data['bmi'].mean(), data['bmi'].std()),
  #                 hind='reg', truncate=True, color='b', height=5, retio=3,
   #                scatter_kws={'s':10,}, line_kws={'lw':1, 'color':'black'})
'''
fig6 = sm.qqplot(data['charges'])#, line='45')
test_stat = sts.kstest(data['charges'], 'norm')
print(test_stat)
plt.show()
'''
data2 = pd.read_csv('ECDCCases.csv')
print('Процентное количество нулевых значений: ', data2.isna().sum().sum() * 100 / len(data2), '%')
data2.drop(['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', 'geoId'], axis=1, inplace=True)
print('С удаленными признаками:', data2.isnull().sum())
data2['countryterritoryCode'].fillna('other', inplace=True)
data2['popData2019'].fillna(data2['popData2019'].median(), inplace=True)
print('Пропусков больше нет:', data2.isnull().sum().sum() * 100 / len(data2), '%')

print(data2.describe())
data2[data2['deaths'] > 3000]['countriesAndTerritories'].unique()
print(len(data2[data2['deaths'] > 3000]['dateRep'].unique()))

data2 = data2.drop_duplicates()

data3 = pd.read_csv('bmi.csv')
data3NW = data3.loc[data3['region'] == 'northwest']['bmi']
data3SW = data3.loc[data3['region'] == 'southwest']['bmi']
print(sts.shapiro(data3NW))
print(sts.shapiro(data3SW))
print(sts.bartlett(data3NW, data3SW))
print(sts.ttest_ind(data3NW, data3SW))

data4 = pd.DataFrame({'N': [1, 2, 3, 4, 5, 6],
                      'Count': [97, 98, 109, 95, 97, 104]})
print(sts.chisquare(data4))

data5 = pd.DataFrame({'Женат': [89,17,11,43,22,1],
                     'Гражданский брак': [80,22,20,35,6,4],
                     'Не состоит в отношениях': [35,44,35,6,8,22]})
data5.index = ['Полный рабочий день','Частичная занятость','Временно неработает','На домохозяйстве','На пенсии','Учёба']
print(sts.chi2_contingency(data5))
