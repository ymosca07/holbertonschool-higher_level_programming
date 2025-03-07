#!/usr/bin/python3
"""Description"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connexion à MySQL avec les arguments passés en ligne de commande
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Création d'un curseur pour exécuter les requêtes
    cur = db.cursor()

    # Exécution de la requête SQL 
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Affichage des résultats ligne par ligne
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
