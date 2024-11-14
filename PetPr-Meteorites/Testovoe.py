import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd;

data = pd.read_csv('PostgreSQL.csv', delimiter=',')
print('По умолчанию выводит первые 5 строк:', '\n',
      data.head(7))
print('Информация о количестве, типе, заполненности данных по столбцам, кол-ве занимаемой памяти:', '\n',
      data.info(), '\n')
print('Вывод количества нулевых значений:', '\n',
      data.isna().sum(), '\n')
# city_name имеет пропуски, а это значит, что для каких-то пользователей это поле было незаполненно
# числовые даннные можно было  бы заполнить, например, медианным значением или самым популярным
# но это всегда необходимо рассматривать ситуативно
# а текстовые данные стоит заполит ьзначением по умолчани, в данном случае это будет default
data.city_name.fillna('default', inplace=True)
print('Выводит True, если строка дублируется:',
      data.duplicated().unique(), '\n')
print('Сводка о числовых данных таблицы (count, mean, std, min, %, max)', '\n',
      data.describe(), '\n')
# функция unique() позволяет посмотреть есть ли True в каких-то строках, но тк выводится только False значит ни какая
# строка не True, ф значит нет ни одного дубликата
print('Проверка, что нет опечаток и данные корректны:', '\n',
      data.course_name.unique(), '\n')
# на небольшой вариативности удобно проверять таким способом корректность данных

fig = plt.figure()
plt.boxplot(data['count_homework_done'], labels=['count_homework_done'], vert=True)
#plt.show()
# можно создать такую для всех числовых данных, но для остальных это не имеет смысла
# по данной диаграмме можно увидеть, что данные не имеют нормального распределения,
# тк усы расмоложены не симетрично относительно медиане (оранжевая линия)
# есть выбросы, данные выходящие за усы

# Преобразование столбцов с датой в datetime и нахождение разницы
data['open_course'] = pd.to_datetime(data['open_course'])
data['course_start'] = pd.to_datetime(data['course_start'])
data['days_between_open_start'] = (data['open_course'] - data['course_start']).dt.days

def func(days):
    if days <= 0:
        return 0
    elif days <= 7:
        return 1
    elif days <= 14:
        return 2
    elif days <= 21:
        return 3
    elif days <= 28:
        return 4
    else:
        return 5


# Распределение по волнам
data['wave'] = data['days_between_open_start'].apply(func)
print(data)
