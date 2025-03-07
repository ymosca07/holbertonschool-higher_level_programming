#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connexion à la base de données MySQL avec les arguments passés en ligne de commande
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        username=sys.argv[1],   # Nom d'utilisateur MySQL
        password=sys.argv[2], # Mot de passe MySQL
        db_name=sys.argv[3],     # Nom de la base de données
        charset="utf8"
    )

    # Création d'un curseur pour exécuter les requêtes SQL
    cur = conn.cursor()

    # Exécution de la requête SQL pour récupérer tous les états triés par id croissant
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération et affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    conn.close()
