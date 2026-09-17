# Référence

Cette page recense les points d'entrée publics actuellement documentés.

## Package

Le package principal est [`axiolock`](https://github.com/axiolock/axiolock/tree/main/axiolock).

## Fonction et compilation

La classe `Function` représente actuellement une fonction décrite par un nom et du code source. La méthode `optimize()` constitue le point d'entrée prévu pour produire une version optimisée.

!!! warning "API expérimentale"

    Cette surface est en cours de construction. Consultez le code source et les notes de version avant de l'intégrer à une application de production.

## Arborescence

- `axiolock/function.py` : représentation d'une fonction et de sa variante optimisée.
- `axiolock/algorithm/` : algorithmes et domaines de compilation.
- `axiolock/_compile/` : mécanismes internes de compilation et de persistance.
- `axiolock/exception/` : exceptions du package.
