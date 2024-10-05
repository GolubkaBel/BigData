import umap
import random
import matplotlib
import pandas as pd
import seaborn as sns
matplotlib.use('TkAgg')
import plotly.express as pe
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.manifold import TSNE
from sklearn.datasets import load_digits



data = pd.read_excel('C:/Users/ksuha/Downloads/Core_CPI_not _seas.xlsx')
data.head()  # Выводит первые 5 строк через print()
dataG = data.loc[:, (data.isna().sum() <= 30)]
# выборка данных по всем строкам, в зависимости от условия накладываемого на столбцы
# Входные данные для loc[] - просто передача исследуемого положения [строки, столбцы]
# Одна метка, например, 5 или 'a'. Обратите внимание, что 5 интерпретируется как метка индекса, а не как целочисленная
# позиция вдоль индекса.
# Список или массив меток, например ['a', 'b', 'c'].
# Объект-срез с метками, например 'a':'f'.  !!! Обратите внимание, что в отличие от обычных срезов python, включены как
# начало, так и конец. !!!
# массив логических значений той же длины, что и разрезаемая ось (строка/столбец), например [True, False, True].
# isna().sum() / isnull().sum() - возвращает количество null
del data
dataG = dataG.apply(lambda x: x.fillna(x.min()), axis=0)
# Я-ебанный гений! Заменяет null значения на минимальное по столбцам
# fillna(что-то) - заменяет null значения на что-то'''

dictXaxes = dict(title='Названия стран', title_font_size=16,
                 tickfont_size=14, tickangle=45,
                 gridwidth=1, gridcolor='pink')

fig1 = go.Figure()  # Создание полотна (сразу с осями, в отличие от matplotlib)
fig1.add_trace(go.Bar(x=dataG.iloc[:, 1:].keys(),
                      y=dataG.iloc[:, 1:].apply(lambda y: y.mean(), axis=0).sort_values(ascending=False),
                      # sort_values - для сортировки Series, ascending - делает её убывающей
                      text=dataG.iloc[:, 1:].apply(lambda y: y.mean(), axis=0).sort_values(ascending=False),
                      # text - подписи значений на столбиках
                      marker=dict(color=list(range(len(dataG.iloc[:, 1:].keys()))),
                                  colorscale='hot', showscale=True,
                                  # cornerradius=30 - не работает, но почему?
                                  line=dict(color='pink', width=2))))

fig1.update_layout(  # Обновление дизайна полотна
    title='Диаграмма непойми чего', title_font_size=18, title_xanchor='center',
    yaxis_title='Количество того самого непойми чего', yaxis_title_font_size=16, yaxis_tickfont_size=14,
    yaxis_gridwidth=1, yaxis_gridcolor='black'
    # margin=dict(l=0, r=0, t=30, b=0)
)
fig1.update_xaxes(dictXaxes)
# Обновление настроек оси X, можно это также делать в update_layout, но надо добавлять xaxis_
# fig1.show()

dictMarker = dict(colors=pe.colors.sequential.Hot,  # list(range(len(dataG.iloc[:, 1:].keys()))),
                  line=dict(color='black', width=2))
dictTitle = dict(title='Диаграмма непойми чего', title_font_size=18,
                 title_x=0.5)
fig2 = go.Figure()
fig2.add_trace(go.Pie(values=dataG.iloc[:, 1:].apply(lambda z: z.mean(), axis=1),
                      labels=dataG.iloc[:, 0], name='Hello!',
                      text=dataG.iloc[:, 0], textinfo='label', textposition='outside',
                      hoverinfo='label+value+percent+name',  # Информация отображающаяся при наведении
                      hole=.3,
                      marker=dictMarker))
fig2.update_layout(dictTitle)
# fig2.show()

fig3 = plt.figure('Графики первых 5 стран по алфавиту', figsize=(10, 10))
plt.plot(dataG.iloc[:, 0], dataG.iloc[:, 1:].apply(lambda o: o.mean(), axis=1),
         label='График средних значений',
         color='forestgreen',
         marker='o', markersize=6, markeredgecolor='black', markeredgewidth=1)
plt.plot(dataG.iloc[:, 0], dataG.iloc[:, 1], label='График значений 1 столбца (Албания)',
         color='lightgreen',
         marker='o', markersize=6, markeredgecolor='black', markeredgewidth=1)
indexCountry = random.randint(1, dataG.shape[0])
plt.plot(dataG.iloc[:, 0], dataG.iloc[:, indexCountry],
         label='График рандомной по идексу страны (%s)' % dataG.keys()[indexCountry],
         color='mediumseagreen',
         marker='o', markersize=6, markeredgecolor='black', markeredgewidth=1)
nameCountry = random.choice(dataG.iloc[:, 1:].keys())
plt.plot(dataG.iloc[:, 0], dataG[nameCountry],
         label='График рандомной по названию страны (%s)' % nameCountry,
         color='darkolivegreen',
         marker='o', markersize=6, markeredgecolor='black', markeredgewidth=1)
plt.plot(dataG.iloc[:, 0], dataG['United States'], label='График США',
         color='limegreen',
         marker='o', markersize=6, markeredgecolor='black', markeredgewidth=1)
plt.xlabel(xlabel='Года', loc='center')
plt.ylabel(ylabel='Показатели чего-то', loc='center')
plt.grid(True, color='mistyrose', linewidth=2)
plt.legend(loc='upper center')
#plt.show()

dataDigits = load_digits()
x, y = load_digits(return_X_y=True)
print(x.shape)
tsneFit = TSNE(n_components=2, perplexity=50, random_state=36)
dataDFit = tsneFit.fit_transform(x)
dataDFitDF = pd.DataFrame(dataDFit, columns=['x', 'y'])
# Если необходимо объединить столбцы разных данных - np.column_stack((um, targets[:3000]))

fig4 = plt.figure()
sns.scatterplot(x='x', y='y', hue=y, data=dataDFitDF, palette='pastel')
#plt.show()

fig5, ax = plt.subplots(2, 3)
nNeight = (5, 25, 50)
minDist = (0.1, 0.6)
for i in range(len(nNeight)):
    for j in range(len(minDist)):
        dataD2FitDF = pd.DataFrame(umap.UMAP(n_neighbors=nNeight[i], min_dist=minDist[j]).fit_transform(x),
                                   columns=['x', 'y'])
        ax[j][i].scatter(x=dataD2FitDF['x'], y=dataD2FitDF['y'], c=y)
plt.show()
