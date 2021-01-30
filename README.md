# Coursera - Automated Reasoning - Satisfiability


## Introduction

These are my solutions to the honorary assignments for the course:

* Extended Sudoku
* Job Scheduling
* Truck Loading
* Program Correctness

The Python scripts generate an SMT format file that should be executed
with the Z3 Theorem solver.

## Dependencies

To run the generated SMT files you need the Z3 Theorem prover installed.

You can get it here:

https://github.com/Z3Prover/z3


## Usage

```
python3 <solution>.py <args> > <solution>.smt && z3 -smt2 <solution>.smt
```
