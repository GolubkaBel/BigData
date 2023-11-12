import numpy as np
import pandas as pd
import scipy.stats as sts
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def MSE(x, w0, w1, y):
    yPred = w1 * x[:, 0] + w0
    return ((y - yPred)**2).mean()


def gradMSE(x, w0, w1, y):
    yPred = w1 * x[:, 0] + w0
    return np.array([2/len(x)*np.sum((y - yPred)) * (-1),
                     2/len(x)*np.sum((y-yPred) * (-x[:, 0]))])





day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
street = [80, 98, 75, 91, 78]
garage = [100, 82, 105, 89, 102]
print(np.corrcoef(street, garage)[0, 1])
data = pd.DataFrame({'street': street, 'garage': garage})
print(data['street'].corr(data['garage']))

plt.grid(True)
plt.title('Диаграмма рассеяния')
plt.scatter(street, garage, marker='o', color='crimson')
# plt.show()

redWines = pd.read_csv('winequality-red.csv', delimiter=';')
# print(data2.info())
print(redWines.corr()['fixed acidity'])

model = LinearRegression()
x = np.array(redWines[['pH']], type(float))
y = np.array(redWines['fixed acidity'], type(float))
model.fit(x, y)
eps = 0.0001
w0 = 0
w1 = 0
learningRate = 0.03
nextW0 = w0
nextW1 = w1
curW0 = nextW0
curW1 = nextW1
n = 100000
for i in range(n):
    curW0 = nextW0
    curW1 = nextW1
    nextW0 = curW0 - learningRate * gradMSE(x, curW0, curW1, y)[0]
    nextW1 = curW1 - learningRate * gradMSE(x, curW0, curW1, y)[1]
    if (abs(curW0 - nextW0) <= eps) and (abs(curW1 - nextW1) <= eps):
        break

yPredAuto = model.coef_[0] * x + model.intercept_
print('\nУгол наклона: ', model.coef_[0], ', ', curW1,
      '\nКоэффициент сдвига: ', model.intercept_, ', ', curW0,
      '\nMSE: ', mean_squared_error(y, yPredAuto), ', ', MSE(x, curW0, curW1, y))
yPred = curW1 * x + curW0
fig = plt.figure()
plt.plot(x, yPredAuto, linewidth=2, color='r',
         label=f'y={model.coef_[0]:.1f}x + 33.8')
plt.plot(x, yPred, linewidth=2, color='g')
plt.scatter(x, y, alpha=0.7)
plt.grid()
# plt.show()

data = pd.read_csv('insurance.csv')
print(data['region'].unique())
groups = data.groupby('region').groups
sw = data['bmi'][groups['southwest']]
se = data['bmi'][groups['southeast']]
nw = data['bmi'][groups['northwest']]
ne = data['bmi'][groups['northeast']]
print(sts.f_oneway(sw, se, nw, ne))

model2 = ols('bmi ~ region', data=data).fit()
print(sm.stats.anova_lm(model2, typ=2))

r = [sw, se, nw, ne]
rName = ['southwest', 'southeast', 'northwest', 'northeast']
for i, val in enumerate(r):
    for j in range(i+1, len(r)):
        print(rName[i], '-', rName[j], ': ', sts.ttest_ind(val, r[j]))
print('Bonferroni: ', 0.05/6)

tukey = pairwise_tukeyhsd(endog=data['bmi'], groups=data['region'], alpha=0.05)
tukey.plot_simultaneous()
plt.vlines(x=data['bmi'].mean(), ymin=-0.5, ymax=4.5, color='r')
tukey.summary()
plt.show()

model3 = ols('bmi ~ C(region) + C(sex) + C(region):C(sex)', data=data).fit()
print(sm.stats.anova_lm(model3, typ=2))
