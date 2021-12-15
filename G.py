import pandas as pd
import matplotlib.pyplot as plt

Titanic = pd.read_csv('titanic.csv')

Titanic['Survived'].fillna(0,inplace=True)
Titanic.drop(Titanic.loc[Titanic['Survived'] == 0].index,inplace=True)
TitanicGroup = Titanic.groupby(['Pclass'], as_index=False)['Survived'].count()

print(TitanicGroup)
