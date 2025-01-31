liste = [("Pierre", "Dos", 10), ("Paul", "Brasse", 13), ("Léa", "Crawl", 6), ("Léa", "Brasse", 8)]
commandes = {
    "1": "ajout_performance",
    "2": "ajout_individu",
    "3": "ajout_nage",
    "4": "liste_performances",
    "5": "liste_nageur",
    "6": "liste_nage",
    "7": "sauvegarde",
    "8": "chargement",
    "0": "quitter"
}

def ajout_performance(liste):
    """Ajoute une performance à la liste"""
    nom = input("Nom du nageur : ")
    nage = input("Type de nage : ")
    longueur = int(input("Nombre de longueurs : "))
    liste.append((nom, nage, longueur))

def ajout_individu(liste):
    """Ajoute un individu sans performance"""
    nom = input("Nom du nageur : ")
    liste.append((nom, "", 0))

def ajout_nage():
    """Ajoute une nouvelle nage"""
    nage = input("Nom de la nouvelle nage : ")
    print(f"La nage {nage} a été ajoutée.")

def liste_performances(liste):
    """Affiche toutes les performances des nageurs"""
    print("Prénom      |  Nage   |  Longueur")
    print("---------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]}")

def liste_nageur(liste):
    """Affiche toutes les performances d'un nageur"""
    tmp = input("Quel nageur ? ")
    print(f"Performances de {tmp}")
    print("  Nage   |  Longueur")
    print("--------------------")
    for elt in liste:
        if elt[0] == tmp:
            print(f" {elt[1]:8}|  {elt[2]}")

def liste_nage(liste):
    """Affiche tous les nageurs pratiquant une nage"""
    tmp = input("Quelle nage ? ")
    print(f"Nage : {tmp}")
    print(" Nageur     |  Longueur")
    print("------------------------")
    for elt in liste:
        if elt[1] == tmp:
            print(f" {elt[0]:11}|  {elt[2]}")

def sauvegarde(liste, filename="save.csv"):
    """Sauvegarde la BDD"""
    with open(filename, 'w') as fichier:
        for elt in liste:
            fichier.write(f"{elt[0]},{elt[1]},{elt[2]}\n")

def chargement(liste, filename="save.csv"):
    """Charge la BDD"""
    with open(filename, 'r') as fichier:
        for line in fichier:
            line = line.strip()
            if line and line[0] != '#':
                tmp = line.split(',')
                liste.append((tmp[0], tmp[1], int(tmp[2])))

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
        sauvegarde(liste)
    elif choix == "8":
        chargement(liste)
    elif choix == "0":
        if quitter():
            break
    else:
        print("Commande inconnue, veuillez réessayer.")