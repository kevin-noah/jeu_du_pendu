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


# partie complète et retourne True (victoire) ou False (défaite).
def jouer(fichier_mots):
    mots = charger_mots(fichier_mots)
    mot_original = choisir_mot(mots)
    # mot_original est conservé pour l'affichage final ; mot sert aux comparaisons internes
    mot = supprimer_accents(mot_original)
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