import time
import matplotlib
import pandas as pd
matplotlib.use('TkAgg')
# from apyori import apriori
import matplotlib.pyplot as plt
from fpgrowth_py import fpgrowth
from apriori_python import apriori
# from efficient_apriori import apriori

data = pd.read_csv('data.csv', delimiter=',')
fig1 = plt.figure()
data.stack().value_counts(normalize=True).iloc[0:19].plot(kind='bar')
fig2 = plt.figure()
data.stack().value_counts().apply(lambda item: item/data.shape[0]).iloc[0:19].plot(kind='bar')
plt.show()

data = pd.read_csv('Market_Basket_Optimisation.csv', delimiter=',')
transaction = []
for i in range(data.shape[0]):
    transaction.append(data.iloc[i].dropna().tolist())
t = []
startTime = time.perf_counter()
tt, rules = apriori(transaction, minSup=0.04, minConf=0.2)
t.append(time.perf_counter() - startTime)
print(len(rules))
for i in range(len(rules)):
    print(rules[i])

'''
# for apyori
rules = apriori(transaction, min_support=0.035, min_confidence=0.2, min_lift=1.0001)
rules = list(rules)'''

'''
# for efficient_apriori
tt, rules = apriori(transaction, min_support=0.04, min_confidence=0.2)'''

tt, rules = fpgrowth(transaction, minSupRatio=0.04, minConf=0.2)
t.append(time.perf_counter() - startTime)
print(len(rules))
for i in range(len(rules)):
    print(rules[i])
