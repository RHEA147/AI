from sklearn import datasets
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn import preprocessing

data = pd.read_csv('laptop.csv')
label_encoder = LabelEncoder()

features = ["CPU","Graphics","SSD","Screen_Size","Price"]
target = "Purchase"

print("Features : ", features)

print("Target : ", target)

data[features] = data[features].apply(preprocessing.LabelEncoder().fit_transform)

X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.3, random_state=42)
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))