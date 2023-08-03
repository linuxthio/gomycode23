import io
import json
import sqlite3
import os
from pathlib import Path

path = Path(os.path.abspath(__file__))
datas = path.parent / "bigbata.db"
# Etablir une connexion a la base de données
connection = sqlite3.connect(datas)
# Creer un curseur
cursor = connection.cursor()
files = []

for file in os.listdir(path.parent):
    if file != "fou.py" and file != "bigbata.db":
        files.append(file)


# for i, dat in enumerate(files, 1):
#     with io.open(path.parent / dat, "r", encoding='utf-8') as file:
#         json_string = file.read()
#         data = json.loads(json_string)
#         # print(data["Source"])
#         # Definir la requete d'insertion
#         insert_query = "INSERT INTO big_data (id, source, information, utilisation, modification, gloabaldata) VALUES (?, ?, ?, ?, ?, ?)"
            
#         # Convertir les valeurs du dictionnaire en chaines de caracteres
#         valu = [str(valu) for valu in data["GlobalData"]]
#         result = ",".join(valu)
#         # Fournir les valeurs a inserer
#         values = (i, data["Source"], data["Information"], data["Utilisation"], data["Modification"], result)

#         # Executer la requete d'insertion
#         cursor.execute(insert_query, values)

#         # Valider la transaction et fermer la connexion
#         connection.commit()

# # Fermer la connexion de base de donnees
# connection.close()

# def delate(name_table, indice):        
#     cursor.execute(f"DELETE from {name_table} where id = {indice}")
#     cursor.connection.commit()  

# for i in range(1, 75):
#     delate("big_data", i) 
print(len(files))