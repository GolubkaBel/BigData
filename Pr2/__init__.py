from statistics import mean
import pandas as pd
import plotly.graph_objs as go
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def avg(param, redWinesList):
    for x in redWines['quality'].unique():
        redWinesList.append(mean(redWines.loc[redWines['quality'] == x][param]))


redWines = pd.read_csv('winequality-red.csv', delimiter=';')
redWines = redWines.sort_values(by='quality')
redWinesAlcoholAVG = []
avg('alcohol', redWinesAlcoholAVG)

print('Info: ')
redWines.info()

print('\nAlcohol AVG: ', redWinesAlcoholAVG)

print('\nFirst 10 str:')
print(redWines.head(10))

print('\nSame str:')
redWines.isna().sum()

fig1 = go.Figure()
fig1.add_trace(go.Bar(x=redWines['quality'].unique(), y=redWinesAlcoholAVG,
                      marker=dict(color=list(range(len(redWines['quality'].unique()))),
                                  coloraxis='coloraxis', line=dict(dict(color='black', width=2)))))
fig1.update_layout(title='dependence of quality on alcohol',
                   title_font_size=20, title_x=0.5,
                   title_xanchor='center', title_yanchor='top',
                   xaxis_title='quality', xaxis_title_font_size=16,
                   yaxis_title='alcohol, º', yaxis_title_font_size=16,
                   height=700, margin=dict(l=0, r=0))
fig1.update_xaxes(tickangle=315, tickfont_size=14,
                  gridwidth=2, gridcolor='ivory')
fig1.update_yaxes(tickfont_size=14, gridwidth=2, gridcolor='ivory')
fig1.show()

fig2 = go.Figure()
fig2.add_trace(go.Pie(values=redWinesAlcoholAVG, labels=redWines['quality'].unique(),
                      marker_line=dict(color='black', width=2)))
fig2.update_layout(title='dependence of quality on alcohol(go.pie)',
                   title_font_size=20, title_x=0.5,
                   title_xanchor='center', title_yanchor='top',
                   xaxis_title='quality', xaxis_title_font_size=16,
                   yaxis_title='alcohol, º', yaxis_title_font_size=16,
                   height=700, margin=dict(l=0, r=0))
fig2.show()

plt.figure(figsize=(10, 10))
plt.plot(redWines['quality'].unique(), redWinesAlcoholAVG,
         label='alcohol', color='green',
         marker='o', markersize=8,
         markeredgecolor='black', markeredgewidth=2)
redWinesFixedAcAVG = []
redWinesResidualSugarAVG = []
redWinesFreeSulfurDioxideAVG = []
avg('fixed acidity', redWinesFixedAcAVG)
avg('residual sugar', redWinesResidualSugarAVG)
avg('free sulfur dioxide', redWinesFreeSulfurDioxideAVG)
plt.plot(redWines['quality'].unique(), redWinesFixedAcAVG,
         label='fixed acidity', color='crimson',
         marker='o', markersize=8,
         markeredgecolor='black', markeredgewidth=2)
plt.plot(redWines['quality'].unique(), redWinesResidualSugarAVG,
         label='residual sugar', color='blue',
         marker='o', markersize=8,
         markeredgecolor='black', markeredgewidth=2)
plt.plot(redWines['quality'].unique(), redWinesFreeSulfurDioxideAVG,
         label='free sulfur dioxide', color='aquamarine',
         marker='o', markersize=8,
         markeredgecolor='black', markeredgewidth=2)
plt.grid(True, color='mistyrose', linewidth=2)
plt.xlabel('alcohol', fontsize=16)
plt.ylabel('parameters', fontsize=16)
plt.title('dependence of quality on ', fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend()
plt.show()

