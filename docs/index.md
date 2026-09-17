# Axiolock

**Compilation algorithmique à partir d'axiomes et de structures verrouillées.**

Axiolock explore une approche où des propriétés connues sur les entrées et les sorties d'une fonction permettent de sélectionner une implémentation plus efficace, tout en conservant un repli vers le comportement original lorsque les conditions ne sont pas réunies.

<div class="grid cards" markdown>

-   :material-download: **Installer**

    ---

    Installez la dernière version publiée avec `pip`.

    [:octicons-arrow-right-24: Installation](getting-started.md)

-   :material-lightbulb-on-outline: **Comprendre**

    ---

    Découvrez le rôle des axiomes, de la compilation et du cache.

    [:octicons-arrow-right-24: Concepts](concepts.md)

-   :material-github: **Contribuer**

    ---

    Le projet est ouvert aux retours, exemples et implémentations.

    [:octicons-arrow-right-24: GitHub](https://github.com/axiolock/axiolock)

</div>

!!! warning "Projet en développement"

    Axiolock est encore en phase alpha. L'API peut évoluer avant la première version stable.

## Vue d'ensemble

Le flux visé est le suivant :

1. Décrire une fonction et ses contraintes.
2. Déclarer les axiomes applicables à ses arguments ou à son résultat.
3. Compiler une variante optimisée pour les cas où ces axiomes sont satisfaits.
4. Utiliser la version originale comme solution de repli dans les autres cas.

## Licence et citation

Axiolock est distribué sous licence MIT. Les informations de citation sont disponibles dans [`CITATION.cff`](https://github.com/axiolock/axiolock/blob/main/CITATION.cff).
