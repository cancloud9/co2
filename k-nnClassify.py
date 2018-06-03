import pandas as pd

df0 = pd.read_csv('sensorData0.csv')
data = list()
target = [0] * len(df0)
for i in range(len(df0)):
    data.append(list(df0.iloc[i,:]))

df1 = pd.read_csv('sensorData1.csv')
target.extend([1] * len(df1))
for i in range(len(df1)):
    data.append(list(df1.iloc[i,:]))

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=13)
model.fit(data, target)
predict = model.predict(data)

err = 0
for i in range(len(df0) + len(df1)):
    if predict[i] != target[i]:
        err += 1

print('accuracy:', 1 - (err / (len(df0) + len(df1))))