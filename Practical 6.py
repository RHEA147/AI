#Adaboost 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('laptop.csv')

label_encoder = LabelEncoder()
data['CPU'] = label_encoder.fit_transform(data['CPU'])
data['Graphics'] = label_encoder.fit_transform(data['Graphics'])
data['SSD'] = label_encoder.fit_transform(data['SSD'])
data['Screen_Size'] = label_encoder.fit_transform(data['Screen_Size'])
data['Price'] = label_encoder.fit_transform(data['Price'])

X = data.drop('Purchase', axis=1)
y = data['Purchase']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=None)

model = AdaBoostClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
