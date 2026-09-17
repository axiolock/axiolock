<div align="center">

> $$\Huge _\Sigma$$
> $$\mathcal{\Huge Axiolock}$$
> ![GitHub language count](https://img.shields.io/github/languages/count/axiolock/axiolock?style=flat-square&logo=python&logoColor=%234380FA&color=%234380FA&link=https%3A%2F%2Fdocs.python.org%2F3%2F)![GitHub License](https://img.shields.io/github/license/axiolock/axiolock?style=flat-square&logoColor=%234380FA&color=%234380FA&link=https%3A%2F%2Fgithub.com%2Faxiolock%2Faxiolock%2Fblob%2Fmain%2FLICENSE)![GitHub commit activity](https://img.shields.io/github/commit-activity/t/axiolock/axiolock?style=flat-square&link=https%3A%2F%2Fgithub.com%2Faxiolock%2Faxiolock%2Fcommits%2Fmain)
>
> $^\textit{A Python library for algorithmic compilation based on axioms and locked structures.}$

    

</div>


## What is Axiolock?

Axiolock is a Python library that enables the creation of more efficient functions by leveraging the power of axioms and locked structures. It allows users to define a set of axioms that the arguments of a function, including its output, may satisfy within a high probability. Based on these probabilistic guarantees, the library can then compile the function into a more efficient version that is guaranteed to produce the same results for any inputs that satisfy the axioms, otherwise the function will be executed in its original form.

Due to the fact that the preprocessing of the functions generally requires a lot of time, the library provides a caching mechanism that allows the user to store the compiled functions for later use. This way, the user can avoid recompiling the same function multiple times.


## Installation

```bash
python -m pip install axiolock
```

## Citing the project

Citation metadata is available in [CITATION.cff](CITATION.cff). GitHub uses this file
to provide the **Cite this repository** option.
