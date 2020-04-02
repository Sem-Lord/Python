# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.


df1 = pd.read_csv('/kaggle/input/ebola-outbreak-20142016-complete-dataset/ebola_2014_2016_clean.csv')
df1.describe()

df = pd.read_csv('/kaggle/input/velib-stat/velib-disponibilite-en-temps-reel.csv', sep=";")
df.head(1398)

print("Le nombre de vélos total mis a la disposition par tout les stations velib est", df['Capacité de la station'].sum())

dispo = (df['Nombre total vélos disponibles'].sum())
dispo_p = ((df['Nombre total vélos disponibles'].sum())*100)/43462
print("Sur la totalite des velos mis a dispositions des station velib; par jour il n'en reste que: ", dispo_p,"%", "soit ", dispo, "velos")


colonnes = ['Nom station','Station en fonctionnement']

fonctionne = df.loc[df['Station en fonctionnement'] == 'NON']
print(df.loc[(df['Station en fonctionnement'] == 'NON'),colonnes], "\n")

print("Parmis les 1398 station y en a que", len(fonctionne), "qui ne fonctionne pas\n")
#compte = fonctionne.count
#fonctionne_chiffre= sum(compte)/len(fonctionne)
print("Soit", (len(fonctionne)*100)/1398,"%", "de l'effectif total\n")


ville_paris = (df.loc[(df['Nom communes équipées'] == "Paris"),:])
print("Sur les 1398 station de velib en  France y en",len(ville_paris), "a paris\n")

ville_paris_p = (len(ville)*100)/1398

                      


paris_f = (df.loc[(df['Station en fonctionnement'] == "NON") & (df['Nom communes équipées'] == "Paris"),:])
print("Parmi les stations velib y en ", len(paris_f), "qui ne fonctionne pas\n")

paris_t = (df.loc[(df['Station en fonctionnement'] == "OUI") & (df['Nom communes équipées'] == "Paris"),:])
print("Parmis les stations velib y en a ", len(paris_t), "qui fonctionne\n")

#print(len(ville))
#ville_p = (len(ville)*100)/1398
#print(len(ville))

#print("A paris on a ", len(ville), " station vélib; soit ", ville_p, "de l'ensemble des stations velib en France")


velo_e = df['Vélos électriques disponibles'].sum()
velo_m = df['Vélos mécaniques disponibles'].sum()

print("Grace au stats sur les velos disponible on remarque: ", velo_e,"velo electriques disponible et", velo_m, "velos mecanique disponible\n")
print("Soit carrement le double du nombre de velos electrique disponible; Ce qui montre clairement la preferences des utilisateurs pour les velib electrique")

#plt.figure(figsize=(20, 20))
#df.hist(column='Nom station',by='Station en fonctionnement')

#(df['Vélos électriques disponibles'] == 0).value_counts().plot.pie()
#plt.figure(figsize=(20, 10))
#(df['Vélos électriques disponibles']).value_counts().plot.pie()


plt.figure(figsize=(20, 15))
plt.subplot2grid((2,1), (0, 0))
(df['Nombre total vélos disponibles']).value_counts(normalize=True).plot(kind="bar", alpha=1)
#(df['Vélos mécaniques disponibles']).value_counts(normalize=False).plot(kind="bar", alpha=1)
plt.title("Stat sur les vélos disponible")
plt.show()


plt.figure(figsize=(20, 10))
df['Station en fonctionnement'].value_counts().plot.pie()



plt.figure(figsize=(20, 15))
df['Nom communes équipées'].value_counts().plot.pie()



f.describe(include='all')

print(df.count())

df.info()


import pandas as pd
velib_disponibilite_en-temps-reel = pd.read_csv("../input/velib-disponibilite-en-temps-reel.csv")