# 2048 (Python + Tkinter)

Implémentation du jeu [2048](https://play2048.co/) en Python avec une interface graphique Tkinter.

## Prérequis

- Python 3.x
- Tkinter (inclus avec la plupart des installations Python sur Windows et macOS ; sur certaines distributions Linux, installer le paquet `python3-tk`)

## Lancer le jeu

```bash
python 2048.py
```

## Contrôles

| Touche | Action |
|--------|--------|
| ↑ | Déplacer vers le haut |
| ↓ | Déplacer vers le bas |
| ← | Déplacer vers la gauche |
| → | Déplacer vers la droite |

## Règles

- Fusionnez les tuiles de même valeur en les faisant glisser dans une direction.
- L’objectif est d’obtenir une tuile **2048**.
- Après chaque mouvement valide, une nouvelle tuile (2 ou 4) apparaît dans une case libre.
- La partie se termine lorsque la grille est pleine et qu’aucun déplacement n’est possible.

## Structure du projet

```
2048/
├── 2048.py      # Jeu (logique + affichage)
├── README.md
└── .gitignore
```
