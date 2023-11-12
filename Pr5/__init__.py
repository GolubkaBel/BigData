import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV as gsc
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

wine = load_wine(as_frame=True)
data = wine.data
target = wine.target
print(data.keys())
data = data.drop('ash', axis=1)

fig1, im = plt.subplots(3, 4)
for i, name in enumerate(data.keys()):
    print(i, ': ', name)
    im[i // 4, i % 4].bar(target, data[name])
    im[i // 4, i % 4].set_title(name)
plt.show()

xTrain, xTest, yTrain, yTest = tts(data, target, train_size=0.8,
                                   shuffle=True, random_state=271)
print(xTest.shape, yTest.shape, xTrain.shape, yTrain.shape)

model1 = LogisticRegression(max_iter=5000, solver='lbfgs', random_state=271)
model1.fit(xTrain, yTrain)
pred = model1.predict(xTest)
print(metrics.classification_report(yTest, pred))
cm = metrics.confusion_matrix(yTest, pred)
fig2 = plt.figure()
sns.heatmap(cm, annot=True, fmt='.10g')
plt.title('LogisticRegression')

param = {'kernel': ('linear', 'rbf', 'poly', 'sigmoid')}
gridSearchSVM = gsc(estimator=SVC(), param_grid=param, cv=6)
gridSearchSVM.fit(xTrain, yTrain)
model2 = gridSearchSVM.best_estimator_
print(model2.kernel)
predKernel = model2.predict(xTest)
print(metrics.classification_report(yTest, predKernel))
cm = metrics.confusion_matrix(yTest, predKernel)
fig3 = plt.figure()
sns.heatmap(cm, annot=True, fmt='.10g')
plt.title('SVM')

param2 = {'n_neighbors': np.arange(3, 10)}
gridSearchSVM2 = gsc(estimator=KNeighborsClassifier(), param_grid=param2, cv=6)
gridSearchSVM2.fit(xTrain, yTrain)
predKNN = gridSearchSVM2.predict(xTest)
print(gridSearchSVM2.best_score_)
print(metrics.classification_report(yTest, predKNN))
cm = metrics.confusion_matrix(yTest, predKNN)
fig4 = plt.figure()
sns.heatmap(cm, annot=True, fmt='.10g')
plt.title('KNN')
plt.show()
