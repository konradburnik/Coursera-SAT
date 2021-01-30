# Coursera - Automated Reasoning - Satisfiability


## Introduction

These are my solutions to the honorary assignments for the course https://www.coursera.org/learn/automated-reasoning-sat

The Python scripts generate an SMT format file that should be executed
with the Z3 Theorem Solver.

## Dependencies

To run the SMT file generator files from this repository you need Python 3.7+ installed:

https://www.python.org/downloads/

To run the generated SMT files you need the Z3 Theorem Solver installed:

https://github.com/Z3Prover/z3


## Usage

```
python3 <solution>.py <args> > <solution>.smt && z3 -smt2 <solution>.smt
```
