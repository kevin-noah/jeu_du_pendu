# Jeu du Pendu

**Auteur :** Kevin Noah  
**Date de remise :** 19 mai 2026

## Description

Implémentation en ligne de commande du jeu du pendu. Le programme choisit aléatoirement un mot dans une liste et invite 
le joueur à le deviner lettre par lettre, avec 6 tentatives autorisées.

Fonctionnalités :
- Gestion native des accents : taper `e` permet de trouver `é`, `è`, `ê`, etc.
- Choix interactif au lancement entre le fichier de mots par défaut et un fichier personnalisé.
- Indice automatique à la dernière chance : une lettre absente du mot est révélée.
- Enchaînement de parties sans quitter le programme.

## Contenu du dépôt

| Fichier | Description |
|---|---|
| `pendu.py` | Script principal — logique du jeu |
| `mots_pendu.txt` | Liste de mots par défaut (126 mots, encodage UTF-8) |
| `README.md` | Documentation du projet |

## Prérequis

- Python 3.6 ou supérieur
- Aucune dépendance externe (bibliothèque standard uniquement)

## Utilisation

Au lancement, le programme demande si vous souhaitez utiliser un fichier de mots personnalisé :

```
Bienvenue au Jeu du Pendu !
Voulez-vous utiliser un fichier de mots personnalisé ? (o/n) :
```

- Répondre `n` : le fichier `mots_pendu.txt` fourni avec le dépôt est utilisé.
- Répondre `o` : le programme demande ensuite le chemin vers votre fichier. Si le fichier est introuvable, la saisie est redemandée.

## Format du fichier de mots personnalisé

Le fichier doit être un fichier texte brut encodé en UTF-8, avec **un mot par ligne** :

```
python
ordinateur
algorithme
éléphant
château
```

Les mots accentués sont acceptés. Les lignes vides sont ignorées.

## Déroulement d'une partie

1. La longueur du mot est affichée (`_ _ _ _ _`).
2. À chaque tour, entrez une lettre. Les lettres déjà proposées sont refusées.
3. Une bonne lettre est révélée à sa (ses) position(s) dans le mot.
4. Une mauvaise lettre est ajoutée à la liste des lettres incorrectes et coûte une tentative.
5. À la dernière tentative, un indice est donné : une lettre qui n'est **pas** dans le mot.
6. La partie se termine par une victoire (mot trouvé) ou une défaite (0 tentative restante).

En fin de partie, le programme propose de rejouer avec le même fichier de mots.
