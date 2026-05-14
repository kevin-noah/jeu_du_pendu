# Jeu du Pendu
****
**Auteur :** Kevin Noah  
**Date de remise :** 18 mai 2026

## Description

Ce projet implémente le classique jeu du pendu en ligne de commande. 
Le programme choisit aléatoirement un mot dans une liste et invite 
le joueur à le deviner lettre par lettre. 

Il gère nativement les accents (le joueur peut entrer `e` pour trouver un `é`), 
accepte un fichier de mots personnalisé en argument, et offre un indice automatique lorsqu'il ne reste qu'une seule chance. 
L'interface est entièrement textuelle et le jeu peut être relancé sans quitter le programme.

## Contenu du dépôt

| Fichier | Description |
|---|---|
| `pendu.py` | Script principal contenant le jeu |
| `mots_pendu.txt` | Liste de mots par défaut |
| `README.md` | fichier de documentation |