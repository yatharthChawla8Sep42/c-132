import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('final.csv')

mass=df['mass'].to_list()
radius=df['radius'].to_list()
gravity=df['gravity'].to_list()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(mass, radius, 'o')
plt.title('Mass vs Radius')
plt.xlabel('Mass')
plt.ylabel('Radius')
plt.show()

plt.plot(mass, gravity, 'o')
plt.title('Mass vs Gravity')
plt.xlabel('Mass')
plt.ylabel('Gravity')
plt.show()
