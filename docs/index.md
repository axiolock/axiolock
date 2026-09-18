# Home

**Algorithmic compilation based on axioms and locked structures.**

Axiolock explores an approach where known properties of a function's inputs and outputs make it possible to select a more efficient implementation, while preserving a fallback to the original behavior when the conditions are not met.

<div class="grid cards" markdown>

-   [:material-download: Installation] **Install**

    ---

    Install the latest release with `pip`.

    [:octicons-arrow-right-24: Getting started](getting-started.md)

-   :material-lightbulb-on-outline: **Understand**

    ---

    Learn about axioms, compilation, and caching.

    [:octicons-arrow-right-24: Concepts](concepts.md)

-   :material-book-open-page-variant-outline: **Reference**
    
    ---

    Browse the API documentation and public entry points.

    [:octicons-arrow-right-24: Référence](reference.md)

-   :material-rocket-launch-outline: **Quick start**

    ---

    Build your first optimized function with Axiolock.

    [:octicons-arrow-right-24: Quick start](getting-started.md)


</div>

!!! warning "Work in progress"

    Axiolock is still in alpha. The API may change before the first stable release.

## Overview

The intended workflow is:

1. Describe a function and its constraints.
2. Declare the axioms that apply to its arguments or result.
3. Compile an optimized variant for cases where those axioms hold.
4. Use the original implementation as a fallback otherwise.

## License and citation

Axiolock is distributed under the MIT license. Citation information is available in [`CITATION.cff`](https://github.com/axiolock/axiolock/blob/main/CITATION.cff).
