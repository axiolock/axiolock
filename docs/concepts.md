# Concepts

## Axioms

An axiom describes an expected property of an input or result. It can express a shape, type, or numeric-domain constraint, for example.

Axioms act as selection conditions: an optimization should only be used when the required properties hold.

## Compilation

Compilation transforms a function representation into a specialized variant. The goal is to move as much expensive work as possible before the actual call while preserving equivalent semantics for admissible inputs.

## Safe fallback

When the axioms do not hold, the original implementation remains the fallback path. This model makes it possible to experiment with specializations without imposing their assumptions on every caller.

## Caching

Preparing a function can cost more than executing it. Axiolock therefore provides persistence so compiled functions can be reused across executions.

!!! note

    These concepts describe the current direction of the project. API details will be refined as the implementation evolves.
