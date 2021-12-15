import pandas as pd
import matplotlib.pyplot as plt

Titanic=pd.read_csv('titanic.csv')

Titanic['Sex']=Titanic['Sex'].replace(['male'],"masculino")
Titanic['Sex']=Titanic['Sex'].replace(['female'],"FEMININO")

print(Titanic)