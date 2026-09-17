# Concepts

## Axiomes

Un axiome décrit une propriété attendue d'une entrée ou d'un résultat. Il peut par exemple exprimer une contrainte de forme, de type ou de domaine numérique.

Les axiomes servent de conditions de sélection : une optimisation ne doit être utilisée que lorsque les propriétés nécessaires sont satisfaites.

## Compilation

La compilation transforme la représentation d'une fonction en une variante spécialisée. L'objectif est de déplacer autant que possible le travail coûteux avant l'appel réel, tout en gardant une sémantique équivalente pour les entrées admissibles.

## Repli sûr

Lorsque les axiomes ne sont pas satisfaits, l'implémentation originale reste le chemin de repli. Ce modèle permet d'expérimenter des spécialisations sans imposer leurs hypothèses à tous les appelants.

## Cache

La préparation d'une fonction peut être plus coûteuse que son exécution. Axiolock prévoit donc un mécanisme de persistance afin de réutiliser les fonctions déjà compilées entre plusieurs exécutions.

!!! note

    Ces concepts décrivent la direction actuelle du projet. Les détails de l'API seront précisés à mesure que l'implémentation évoluera.
