import pandas as pd
import matplotlib.pyplot as plt

Titanic = pd.read_csv('titanic.csv')

Titanic['Survived'].fillna(1,inplace=True)
Titanic.drop(Titanic.loc[Titanic['Survived'] == 1].index,inplace=True)
TitanicDeath = Titanic.groupby('Sex', as_index = False)['Survived'].count()

print(TitanicDeath)