def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            contenu = f.read()
            return contenu
    except FileNotFoundError:
        return "Fichier non trouvé"

def ecrire_fichier(nom_fichier, contenu):
    with open(nom_fichier, 'w') as f:
        f.write(contenu)

contenu = lire_fichier("mon_fichier.txt")
print(contenu)

ecrire_fichier("mon_fichier.txt", "Nouveau contenu")