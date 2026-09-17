# Reference

This page lists the currently documented public entry points.

## Package

The main package is [`axiolock`](https://github.com/axiolock/axiolock/tree/main/axiolock).

## Function and compilation

The `Function` class currently represents a function described by a name and source code. The `optimize()` method is the intended entry point for producing an optimized version.

!!! warning "Experimental API"

    This surface is under construction. Review the source code and release notes before integrating it into a production application.

## Package layout

- `axiolock/function.py`: representation of a function and its optimized variant.
- `axiolock/algorithm/`: compilation algorithms and domains.
- `axiolock/_compile/`: internal compilation and persistence mechanisms.
- `axiolock/exception/`: package exceptions.
