#Naive Bayes

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('products.csv')

label_encoder = LabelEncoder()
data['buying_product'] = label_encoder.fit_transform(data['buying_product'])
X = data.drop('buying_product', axis=1)
y = data['buying_product']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=None)

model = GaussianNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

age = int(input("Enter the age of the customer: "))
income = int(input("Enter the income of the customer: "))

new_data = [[age,income]]
predicted_probability = model.predict_proba(new_data)[:, 1]
predicted_label = 1 if predicted_probability >= 0.5 else 0
print("Predicted probability of buying the product:", predicted_label)
