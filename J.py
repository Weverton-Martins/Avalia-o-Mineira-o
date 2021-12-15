import pandas as pd
import matplotlib.pyplot as plt

Titanic=pd.read_csv('titanic.csv')

Titanic=pd.ExcelWriter('titanic.xlsx')
Titanic.save()
