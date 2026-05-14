from sys import argv
# Point d'entrée : lit l'argument de ligne de commande et enchaîne les parties.

# partie complète et retourne True (victoire) ou False (défaite).
def jouer(fichier_mots):
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