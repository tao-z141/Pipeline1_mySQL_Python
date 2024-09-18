import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="Ecole",
    user="root",
    password="mot de passe",
    port="3306"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM etudiant;")
etudiant = cursor.fetchall()
liste_etudiant = []

for i in etudiant:
    dic_etudiant = {
        "student_id": i[0],
        "nom": i[1],
        "prenom": i[2],
        "numero_salle": i[3],
        "telephone": i[4],
        "email": i[5],
        "annee_obtention": i[6],
        "numero_classe": i[7]
    }
    liste_etudiant.append(dic_etudiant)

print(f"Table Etudiant : \n {liste_etudiant}")

cursor.execute("SELECT * FROM enseignants;")
profs = cursor.fetchall()
liste_prof = []
for prof in profs:
    dic_prof = {
        "teacher_id": prof[0],
        "prenom": prof[1],
        "nom": prof[2],
        "numero_salle": prof[3],
        "departement": prof[4],
        "annee_obtention": prof[5],
        "email": prof[6],
        "telephone": prof[7],
        "numero_classe": prof[8]
    }

    liste_prof.append(dic_prof)

print(f"Table Enseignants : \n {liste_prof}")

cursor.execute("SELECT e.prenom , e.nom , et.prenom , et.nom, e.numero_classe , et.numero_classe  FROM etudiant et JOIN enseignants e on e.numero_classe = et.numero_classe ;")
etudiant_prof = cursor.fetchall()

liste_etudiant_prof = []


for i in etudiant_prof:
    dic_etudiant_prof = {
        "prenom_prof": i[0],
        "nom_prof": i[1],
        "prenom_etudiant": i[2],
        "nom_etudiant": i[3],
        "numero_classe_prof": i[4],
        "numero_classe_etudiant": i[5]
    }

    liste_etudiant_prof.append(dic_etudiant_prof)

print(f"Association etudiant et enseignants : \n {liste_etudiant_prof}")

cursor.execute("SELECT e.prenom , e.nom , count(et.student_id)  FROM etudiant et JOIN enseignants e on e.numero_classe = et.numero_classe  group by e.prenom, e.nom;")
nombre_etudiant_par_prof = cursor.fetchall()

liste_nb_etudiant_par_prof = []
for i in nombre_etudiant_par_prof:
    nb_etudiant = {
        'prenom_prof': i[0],
        'nom_prof': i[1],
        'nombre_etudiant': i[2]
    }
    liste_nb_etudiant_par_prof.append(nb_etudiant)

print(f"Nombre d'etudiant par prof : \n {liste_nb_etudiant_par_prof}")

conn.close()