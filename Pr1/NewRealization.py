import math
from sklearn.datasets import fetch_california_housing


class Shape:
    name = 'none'
    s = 0.0
    r = 0.0
    a = 0.0
    b = 0.0

    def __init__(self, name):
        self.name = name

    def circle(self, r, pi=3.14):
        self.s = r ** 2 * pi

    def rectangle(self, a, b):
        self.s = a * b

    def triangle(self, a, b):
        self.s = 0.5 * a * b

    def printDef(self):
        print('%s; S = %.2f' % (self.name, self.s))


class Operation:
    operator = 'none'
    a = 0.0
    b = 0.0
    result = 0.0

    def __init__(self, operator, a, b):
        self.a = a
        self.b = b
        if operator == '+':
            self.result = a + b
        elif operator == '-':
            self.result = a - b
        elif operator == '/':
            self.result = a / b
        elif operator == '//':
            self.result = a // b
        elif operator == 'abs':
            self.result = math.fabs(a - b)

    def printOperRes(self):
        print('%s -> %.2f' % (self.operator, self.result))


if input('Do u want to launch -Shape-? ').lower() == 'yes':
    shape = Shape(str(input('Shape is ')).lower())
    if shape.name == 'circle':
        shape.circle(int(input('R = ')))
    elif shape.name == 'rectangle':
        shape.rectangle(int(input('a = ')), int(input('b = ')))
    elif shape.name == 'triangle':
        shape.triangle(int(input('a = ')), int(input('b = ')))
    else:
        print('error - type of shape')
    shape.printDef()
elif input('Do u want to launch -Operation-? ').lower() == 'yes':
    operation = Operation(str(input('Operation is ')), int(input('a = ')), int(input('b = ')))
    operation.printOperRes()
elif input('Do u want to launch -Sum=0-? ').lower() == 'yes':
    array = [int(input('Array: '))]
    while sum(array) != 0:
        array.append(int(input()))
    sumOfSquare = 0
    for x in array:
        sumOfSquare = sumOfSquare + x ** 2
    print(sumOfSquare)
elif input('Do u want to launch -ListCount-? ').lower() == 'yes':
    n = int(input('N = '))
    x = 1
    array = [1]
    for i in range(1, n):
        if array.count(x) == x:
            x = x + 1
        array.append(x)
    print(*array)
elif input('Do u want to launch -ConcatinationDict-? ').lower() == 'yes':
    arrayA = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    arrayB = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    dictionary = dict(zip(sorted(set(arrayB)), [0] * len(set(arrayB))))
    for x in arrayB:
        print(dictionary.get(x))
        dictionary[x] = dictionary.get(x) + arrayA[arrayB.index(x)]
        print(' - ', dictionary.get(x))
        arrayB[arrayB.index(x)] = ''
    print(dictionary)
elif input('do u want to launch -HouseOfCalifornia-? ').lower() == 'yes':
    df = fetch_california_housing(as_frame=True)
    df.data.info()
    print(df.data.isna().sum())
    print(df.data.loc[(df.data['HouseAge'] > 50) & (df.data['Population'] > 2500)])
    print(df.data.describe())
    print(df.data.min())

    def func(data):
        return data.mean()

    print(df.data.apply(func, axis=0))
