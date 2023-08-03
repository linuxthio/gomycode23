import json
import sqlite3
import os
from pathlib import Path

path = Path(os.path.abspath(__file__))
datas = path.parent / "bigdata.db"
# Établir une connexion à la base de données
connection = sqlite3.connect(datas)
# Créer un curseur
cursor = connection.cursor()
files = []

for file in os.listdir(path.parent):
    if file != "bigdata.db" and file != "new.py" and file != "fou.py" and file != "bigbata.db":
        files.append(file)   
        
for j, dat in enumerate(files,1):
    with open(path.parent / "datas.json") as file:
        data = json.load(file)
        paysdata = data["PaysData"]
        globaldata = data["GlobalData"]
        # for i,row in enumerate(globaldata,1):
        #     # Définir la requête d'insertion sur la table gloabaldata
        #     insert_query_gloabaldata = "INSERT INTO gloabaldata (date, infection, deces, guerisons, taux_deces, taux_guerison, taux_infection) VALUES (?, ?, ?, ?, ?, ?, ?)"            
        #     # Fournir les valeurs à insérer        
        #     values_gloabaldata = (row["Date"], row["Infection"], row["Deces"], row["Guerisons"],row["TauxDeces"],row["TauxGuerison"],row["TauxInfection"])
        #     # Exécuter la requête d'insertion
        #     cursor.execute(insert_query_gloabaldata, values_gloabaldata)
        #     # Valider la transaction
        #     connection.commit()

        # # Définir la requête d'insertion sur la table info
        # insert_query_info = "INSERT INTO info (source, information, utilisation, modification) VALUES (?, ?, ?, ?)"            
        # # Fournir les valeurs à insérer
        # values_info = (data["Source"], data["Information"], data["Utilisation"], data["Modification"])
        # # Exécuter la requête d'insertion
        # cursor.execute(insert_query_info, values_info)
        # # Valider la transaction
        # connection.commit()
            
        for row in paysdata:
            # Définir la requête d'insertion sur la table paysdata
            insert_query_paysdata = "INSERT INTO paysdata (date, pays, infection, deces, guerisons, taux_deces, taux_guerison, taux_infection) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"            
            # Fournir les valeurs à insérer        
            values_paysdata = (row["Date"], row["Pays"], row["Infection"], row["Deces"], row["Guerisons"],row["TauxDeces"],row["TauxGuerison"],row["TauxInfection"])
            # Exécuter la requête d'insertion
            cursor.execute(insert_query_paysdata, values_paysdata)
            # Valider la transaction
            connection.commit()




# Fermer la connexion à la base de données (en dehors de la boucle)
connection.close()

