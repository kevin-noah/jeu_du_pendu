# ─── Imports ciblés (fonctions utilisées uniquement) ──────────────────────────
from random import choice as choix
from unicodedata import normalize as normalise, category as categorie
from sys import argv, exit

# ─── Chargement des données ────────────────────────────────────────────────────

# Lit le fichier de mots et retourne la liste ; arrête le programme si impossible.
def charger_mots(fichier='mots_pendu.txt'):
    try:
        # Encodage UTF-8 obligatoire pour prendre en charge les caractères accentués
        with open(fichier, 'r', encoding='utf-8') as f:
            # Ignore les lignes entièrement vides ou composées uniquement d'espaces
            mots = [ligne.strip() for ligne in f if ligne.strip()]
        if not mots:
            # Fichier présent mais sans aucun mot utilisable : impossible de jouer
            print(f"Erreur: Le fichier '{fichier}' est vide.")
            exit(1)
        return mots
    except FileNotFoundError:
        # Le fichier est introuvable dans le répertoire courant ou au chemin indiqué
        print(f"Erreur: Le fichier '{fichier}' est introuvable.")
        exit(1)


# Supprime les accents et met le texte en minuscules pour des comparaisons uniformes.
# Permet au joueur de taper 'e' pour trouver 'é', 'è' ou 'ê' sans distinction.
def supprimer_accents(texte):
    # Forme NFD : chaque lettre accentuée est décomposée en base + diacritique séparé
    nfd = normalise('NFD', texte)
    # La catégorie 'Mn' (Mark Nonspacing) correspond aux diacritiques : on les supprime
    return ''.join(c for c in nfd if categorie(c) != 'Mn').lower()


def choisir_mot(mots):
    return choix(mots)

# Affiche le mot : lettre visible si devinée, sinon remplacée par '_'.
def afficher_etat(mot, lettres_devinees):
    # Les espaces entre les caractères améliorent la lisibilité du mot masqué
    etat = ' '.join(c if c in lettres_devinees else '_' for c in mot)
    print(f"Mot : {etat}")

# Révèle une lettre de l'alphabet qui n'est PAS dans le mot (indice négatif).
def donner_indice(mot, lettres_devinees, lettres_incorrectes):
    # L'alphabet complet sert de base pour identifier les lettres disponibles
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # On exclut les lettres du mot et toutes celles déjà connues du joueur
    pas_dans_mot = alphabet - set(mot) - lettres_incorrectes - lettres_devinees
    if pas_dans_mot:
        # Tri avant tirage
        indice = choix(sorted(pas_dans_mot))
        print(f"Indice : la lettre '{indice.upper()}' n'est PAS dans le mot.")


# Boucle de saisie avec validation complète : rejette les entrées invalides et les doublons.
def obtenir_lettre(lettres_devinees, lettres_incorrectes):
    # La boucle tourne jusqu'à obtenir une lettre valide et non encore proposée
    while True:
        saisie = input("Entrez une lettre : ").strip()
        # Refus des saisies vides pour éviter une erreur d'index au caractère suivant
        if not saisie:
            print("Veuillez entrer une lettre.")
            continue
        # On retient uniquement le premier caractère saisi, puis on normalise
        lettre = supprimer_accents(saisie[0])
        # Rejette tout ce qui n'est pas une lettre (chiffres, symboles, espaces, etc.)
        if not lettre.isalpha():
            print("Veuillez entrer une lettre valide (a-z).")
            continue
        # Empêche de soumettre deux fois la même lettre, qu'elle soit correcte ou non
        if lettre in lettres_devinees or lettre in lettres_incorrectes:
            print(f"Vous avez déjà essayé la lettre '{lettre.upper()}'.")
            continue
        return lettre


# partie complète et retourne True (victoire) ou False (défaite).
def jouer(fichier_mots):
    mots = charger_mots(fichier_mots)
    mot_original = choisir_mot(mots)
    # mot_original est conservé pour l'affichage final ; mot sert aux comparaisons internes
    mot = supprimer_accents(mot_original)

    # Initialisation : 6 tentatives et deux ensembles vides pour suivre les lettres
    chances = 6
    # Ensemble des lettres correctement devinées par le joueur
    lettres_devinees = set()
    # Ensemble des lettres proposées qui ne figurent pas dans le mot
    lettres_incorrectes = set()

    # En-tête de la partie : seule la longueur du mot est révélée au départ
    print(f"\n{'='*42}")
    print("           JEU DU PENDU")
    print(f"{'='*42}")
    print(f"Le mot a {len(mot)} lettre(s).\n")

     # Boucle principale : un tour correspond à une lettre proposée par le joueur
    while chances > 0:
        afficher_etat(mot, lettres_devinees)
        print(f"Chances restantes : {chances}")
        if lettres_incorrectes:
            # Affiche les mauvaises lettres en majuscules, triées par ordre alphabétique
            mauvaises = ', '.join(sorted(lettres_incorrectes)).upper()
            print(f"Lettres incorrectes : {mauvaises}")

        # L'indice est offert uniquement lors de la toute dernière tentative restante
        if chances == 1:
            donner_indice(mot, lettres_devinees, lettres_incorrectes)

        lettre = obtenir_lettre(lettres_devinees, lettres_incorrectes)

        if lettre in mot:
            lettres_devinees.add(lettre)
            print(f"Bonne réponse ! '{lettre.upper()}' est dans le mot.")
            # Condition de victoire : chaque lettre du mot a été devinée
            if all(c in lettres_devinees for c in mot):
                afficher_etat(mot, lettres_devinees)
                print(f"\nBravo ! Vous avez trouvé le mot : {mot_original.upper()}")
                return True
        else:
            lettres_incorrectes.add(lettre)
            # Chaque mauvaise réponse coûte une chance au joueur
            chances -= 1
            print(f"Mauvaise réponse ! '{lettre.upper()}' n'est pas dans le mot.")
            # Condition de défaite : le compteur de chances atteint zéro
            if chances == 0:
                afficher_etat(mot, lettres_devinees)
                print(f"\nDommage ! Vous avez perdu. Le mot était : {mot_original.upper()}")
                return False

        # Ligne vide pour séparer visuellement les tours successifs
        print()
    return False

# Demande si le joueur souhaite enchaîner une nouvelle partie et valide sa réponse.
def demander_rejouer():
    # Boucle jusqu'à obtenir une réponse reconnue (o/oui ou n/non)
    while True:
        reponse = input("\nVoulez-vous rejouer ? (o/n) : ").strip().lower()
        # Accepte 'o' (abréviation) et 'oui' (forme longue) pour continuer
        if reponse in ('o', 'oui'):
            return True
        # Accepte 'n' (abréviation) et 'non' (forme longue) pour quitter
        if reponse in ('n', 'non'):
            return False
        print("Veuillez entrer 'o' pour oui ou 'n' pour non.")

# Point d'entrée : lit l'argument de ligne de commande et enchaîne les parties.
def main():
    # Utilise le fichier passé en argument ou le fichier par défaut si aucun n'est fourni
    fichier_mots = argv[1] if len(argv) > 1 else 'mots_pendu.txt'
    print("Bienvenue au Jeu du Pendu !")
    # La boucle s'arrête uniquement quand le joueur refuse de rejouer
    while True:
        jouer(fichier_mots)
        if not demander_rejouer():
            print("Merci d'avoir joué ! Au revoir !")
            break

# Entree du programme
main()