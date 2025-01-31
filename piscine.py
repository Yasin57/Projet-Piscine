from datetime import datetime
from get_value import get_int_value

liste = [("Pierre", "Dos", 10, "2024-05-11"), ("Paul", "Brasse", 13, "2024-05-12"), ("Léa", "Crawl", 6, "2024-05-11"), ("Léa", "Brasse", 8, "2024-05-13")]
commandes = {
    "1": "ajout_performance",
    "2": "ajout_individu",
    "3": "ajout_nage",
    "4": "liste_performances",
    "5": "liste_nageur",
    "6": "liste_nage",
    "7": "liste_date",
    "8": "sauvegarde",
    "9": "chargement",
    "0": "quitter"
}

def ajout_performance(liste):
    """Ajoute une performance à la liste"""
    nom = input("Nom du nageur : ")
    nage = input("Type de nage : ")
    longueur = get_int_value()
    date = input("Date (YYYY-MM-DD) : ")
    liste.append((nom, nage, longueur, date))

def ajout_individu(liste):
    """Ajoute un individu sans performance"""
    nom = input("Nom du nageur : ")
    liste.append((nom, "", 0, ""))

def ajout_nage():
    """Ajoute une nouvelle nage"""
    nage = input("Nom de la nouvelle nage : ")
    print(f"La nage {nage} a été ajoutée.")

def liste_performances(liste):
    """Affiche toutes les performances des nageurs"""
    print("Prénom      |  Nage   |  Longueur | Date")
    print("-----------------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]:8}| {elt[3]}")

def liste_nageur(liste):
    """Affiche toutes les performances d'un nageur et leurs statistiques"""
    tmp = input("Quel nageur ? ")
    performances = [elt[2] for elt in liste if elt[0] == tmp]
    
    if performances:
        print(f"Performances de {tmp}")
        print("  Nage   |  Longueur | Date")
        print("--------------------------------")
        for elt in liste:
            if elt[0] == tmp:
                print(f" {elt[1]:8}|  {elt[2]:8}| {elt[3]}")
        print("--------------------------------")
        print(f"Minimum : {min(performances)}")
        print(f"Maximum : {max(performances)}")
        print(f"Moyenne : {sum(performances) / len(performances):.1f}")
    else:
        print("Aucune performance trouvée pour ce nageur.")

def liste_nage(liste):
    """Affiche tous les nageurs pratiquant une nage"""
    tmp = input("Quelle nage ? ")
    print(f"Nage : {tmp}")
    print(" Nageur     |  Longueur | Date")
    print("--------------------------------")
    for elt in liste:
        if elt[1] == tmp:
            print(f" {elt[0]:11}| {elt[2]:8}| {elt[3]}")

def liste_date(liste):
    """Affiche toutes les performances enregistrées à une date donnée"""
    date_recherche = input("Quelle date (YYYY-MM-DD) ? ")
    print(f"Performances du {date_recherche}")
    print(" Nageur     |  Nage   |  Longueur")
    print("--------------------------------")
    for elt in liste:
        if elt[3] == date_recherche:
            print(f" {elt[0]:11}| {elt[1]:8}| {elt[2]:8}")

def sauvegarde(liste, filename="save.csv"):
    """Sauvegarde la BDD"""
    with open(filename, 'w') as fichier:
        for elt in liste:
            fichier.write(f"{elt[0]},{elt[1]},{elt[2]},{elt[3]}\n")

def chargement(liste, filename="save.csv"):
    """Charge la BDD"""
    with open(filename, 'r') as fichier:
        for line in fichier:
            line = line.strip()
            if line and line[0] != '#':
                tmp = line.split(',')
                liste.append((tmp[0], tmp[1], int(tmp[2]), tmp[3]))

def quitter():
    """Quitte le logiciel"""
    confirmation = input("En êtes-vous sûr ? (o)ui/(n)on : ")
    return confirmation.lower() != 'o'

while True:
    print("\nMenu :")
    for key, value in commandes.items():
        print(f"{key} -> {value.replace('_', ' ')}")
    choix = input("Votre choix : ")
    
    if choix == "1":
        ajout_performance(liste)
    elif choix == "2":
        ajout_individu(liste)
    elif choix == "3":
        ajout_nage()
    elif choix == "4":
        liste_performances(liste)
    elif choix == "5":
        liste_nageur(liste)
    elif choix == "6":
        liste_nage(liste)
    elif choix == "7":
        liste_date(liste)
    elif choix == "8":
        sauvegarde(liste)
    elif choix == "9":
        chargement(liste)
    elif choix == "0":
        if quitter():
            break
    else:
        print("Commande inconnue, veuillez réessayer.")
