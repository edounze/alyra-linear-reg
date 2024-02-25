import sqlite3 as sq
import matplotlib.pyplot as plt
import numpy as np
import random as rd

from sklearn.linear_model import LinearRegression

# Connexion
connect = sq.connect('data.db')

cursor = connect.cursor()

# Création de la table
cursor.execute("""
    CREATE table if not exists user (
               id integer primary key autoincrement, 
               name varchar(100), 
               age smallint, 
               tall smallint
    );
""")

# Insertion de données
insertCommand = "INSERT INTO user (name, age, tall) VALUES (?, ?, ?)"
insertValues = []
for index in range(8, 100):
    insertData = ("User " + str(index), rd.randint(15, 84), rd.randint(160, 185))
    insertValues.append(insertData)

cursor.executemany(insertCommand, insertValues)


# Sauvegarde effective des données en BDD
# connect.commit()

# Récupération des données
cursor.execute("select * from user")


allData = cursor.fetchall()

# Fermeture de la connexion
connect.close()


# Préparation des données pour la reg linéaire
xData = []
yData = []
for data in allData:
    xData.append(data[2])
    yData.append(data[3])


# Trie des données pour que les données aient une pente décroissante
xData.sort()
yData.sort(reverse=True) # Avec l'age on est moins grand

xAxis = np.array(xData).reshape((-1, 1))
yAxis = np.array(yData)

#======================
# Affichage graphique
#======================

# Graphique des données
# plt.scatter(xData, yData)
plt.plot(xData, yData, 'ro')

plt.xlabel('Age')
plt.ylabel('Taille')


# Regression linéaire
model = LinearRegression().fit(xAxis, yAxis)
r_sq = model.score(xAxis, yAxis)

# =============================
# Graphique régression linéaire
# =============================

# Conversion de xData en un array NumPy
xData_np = np.array(xData) # Transformation sous forme de matrice
# print('xData : ', xData)
# print('xData_np : ', xData_np)

# exit()

a, b = np.polyfit(xData, yData, 1)


# y = ax + b
graphLabel = 'y = ' + str(a) + 'x + ' + str(b)
plt.plot(xData, a*xData_np+b, color='blue', label=graphLabel)
plt.legend()

# Affichage des graphiques
plt.show()

# Prédiction
print(f"coefficient of determination: {r_sq},", f"intercept: {model.intercept_},", f"slope: {model.coef_}")

dataToPredict = [rd.randint(10, 100), rd.randint(10, 100)]
x_entries = np.array(dataToPredict).reshape((-1, 1))

y_pred = model.predict(x_entries)


print("Données en entrée", dataToPredict)
print('x_entries : ',x_entries)
print(f"predicted response:\n{y_pred}")

print(np.array([1, 2, 3, 4, 5]))