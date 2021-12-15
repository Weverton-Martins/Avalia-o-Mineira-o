import pandas as pd
import matplotlib.pyplot as plt

Titanic=pd.read_csv('titanic.csv')

Titanic=Titanic.drop(columns=['SibSp'])
Titanic=Titanic.drop(columns=['Parch'])
Titanic=Titanic.drop(columns=['Ticket'])

Titanic=Titanic.rename(columns={'PassengerId': 'PassageirosID', 'Survived':'Sobreviventes','Pclass':'Classes', 'Name':'Nome', 'Sex':'Sexo', 'Age':'Idade', 'Fare':'Tarifa', 'Cabin':'Cabine','Embarked':'Embarcados'},inplace=False)
Titanic=Titanic.head(15)

print(Titanic)