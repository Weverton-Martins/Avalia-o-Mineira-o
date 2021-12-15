import pandas as pd
import matplotlib.pyplot as plt

Titanic=pd.read_csv('titanic.csv')
#print(Titanic.head(10))

Titanic2 = Titanic.sort_values(['Name'])
print(Titanic2.head(25))


