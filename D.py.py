#from TitanicPan import Titanic

import pandas as pd
import matplotlib.pyplot as plt

Titanic=pd.read_csv('titanic.csv')

Titanic=Titanic.drop(columns=['SibSp'])
Titanic=Titanic.drop(columns=['Parch'])
Titanic=Titanic.drop(columns=['Ticket'])

Titanic=Titanic.head()
print(Titanic)