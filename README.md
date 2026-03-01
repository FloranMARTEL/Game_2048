# Jeu 2048 avec Algorithme NEAT

## Description

Ce projet implémente une version du jeu 2048 où l'intelligence artificielle utilise l'algorithme NEAT (NeuroEvolution of Augmenting Topologies) pour apprendre à jouer de manière autonome.

## Lancement du projet

### Mode console (entraînement)
```bash
python src/LancerNeat.py
```

### Mode interface graphique
```bash
python src/LancerNeatView.py
```

## Architecture

Le projet est structuré en trois composants principaux :

1. **Jeu 2048** (`src/Game/`) : Logique complète du jeu
2. **Algorithme NEAT** (`src/Neat/`) : Implémentation de l'évolution des réseaux de neurones
3. **Interface graphique** (`src/NeatView/`) : Visualisation et contrôle

## Algorithme NEAT

### Principe
NEAT évolue des réseaux de neurones à travers des générations successives :
- **Population initiale** : 100 individus avec des réseaux simples
- **Évaluation** : Chaque individu joue au 2048 et obtient un score
- **Classification** : Regroupement en espèces selon similarité génétique
- **Sélection** : Meilleurs individus conservés
- **Reproduction** : Crossover entre individus
- **Mutation** : Ajout de neurones/connexions

### Paramètres
- **Entrées** : 16 (état du plateau 4x4)
- **Sorties** : 4 (directions de déplacement)
- **Population** : 100 individus
- **Générations** : 200 (configurable)

## Exemples de résultats d'entraînement

### Évolution des performances

| Génération | Meilleur score | Description |
|------------|----------------|-------------|
| 10 | 5968 | Réseaux simples, performances de base |
| 50 | 20032 | Amélioration significative, réseaux plus complexes |
| 100 | 9184 | Adaptation à des stratégies avancées |

### Analyse des générations

- **Génération 10** : Individus avec des réseaux de base (20 neurones max)
- **Génération 50** : Introduction de neurones cachés, meilleures stratégies
- **Génération 100** : Réseaux complexes avec 30+ neurones, optimisation fine

## Interface graphique

L'interface permet de :
- Visualiser l'évolution des générations
- Observer les meilleurs individus jouer
- Configurer les paramètres de l'algorithme
- Sauvegarder/charger des états d'entraînement

## Fichiers de données

Les fichiers `Generation_*.json` dans `src/Neat/data/` contiennent les sauvegardes des générations pour reprendre l'entraînement ou analyser les résultats.

## Dépendances

- Python 3.x
- Tkinter (pour l'interface graphique)
- NumPy (pour les calculs)
- json (pour la sauvegarde des données)

## Licence

MIT License - voir fichier LICENSE
