#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connexion à MySQL avec les arguments passés en ligne de commande
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],   # Nom d'utilisateur MySQL
        passwd=sys.argv[2], # Mot de passe MySQL
        db=sys.argv[3],     # Nom de la base de données
    )

    # Création d'un curseur pour exécuter les requêtes SQL
    cur = db.cursor()

    # Exécution de la requête SQL pour récupérer tous les états triés par ID croissant
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Affichage des résultats ligne par ligne
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
