import pandas as pd
import matplotlib.pyplot as plt

Titanic=pd.read_csv('titanic.csv')

Titanic['Sobrevivente']=Titanic['Survived']
Titanic['Sobrevivente']=Titanic['Sobrevivente'].replace([1],'Sim')
Titanic['Sobrevivente']=Titanic['Sobrevivente'].replace([0],'Não')

print(Titanic)

