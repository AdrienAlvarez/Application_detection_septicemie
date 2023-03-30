#Import des librairies
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

#Import du fichier csv
df = pd.read_csv('/content/data_sepsis.csv')

#Numérisation de la colonne "Sespssis" 
df['Sepssis'] = df['Sepssis'].apply(lambda x: 1 if x == 'Positive' else 0)

#Suppression de la colonne ID
df = df.drop('ID', axis=1)

# Séparation des données en ensembles d'apprentissage et de test
X = df.drop('Sepssis', axis=1)
y = df['Sepssis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

#Modèle de regression
model = LogisticRegression()
model.fit(X_train, y_train)

#Prédiction
y_pred = model.predict(X_test)

#Evaluation du modèle 
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print('Accuracy:', accuracy)
print('Recall:', recall)
print('Precision:', precision)
print('F1 Score:', f1)

# Sauvegarde du modèle
import pickle
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
