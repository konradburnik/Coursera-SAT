import sys

"""

 Hadamard Matrix Finder - not course related

"""


def declare_variables(letter, n):
    vars = [
        f'(declare-const {letter}_{i+1}_{j+1} Int)' for i in range(n) for j in range(n)]
    return '\n'.join(vars)


def value_constraints(letter, n):
    cons = [f'(or (= {letter}_{i+1}_{j+1} 1) (= {letter}_{i+1}_{j+1} -1))' for i in range(n)
            for j in range(n)]
    return '\n'.join(cons)


def symmetry_constraints(letter, n):
    sym = [f'(= {letter}_{i+1}_{j+1} {letter}_{j+1}_{i+1})' for i in range(n)
           for j in range(n)]
    return '\n'.join(sym)


def circulant_matrix_constraints(letter, n):
    circulant = [
        f'(= {letter}_{i+1}_{j+1} {letter}_{1}_{(j-i) % n + 1})' for i in range(1, n) for j in range(n)]
    return '\n'.join(circulant)


def sum_matrix_expression(mats, n):
    result = []
    for i in range(n):
        for j in range(n):
            row = []
            for letter1, letter2 in mats:
                row.append(matrix_mult_element_expression(
                    letter1, letter2, i, j, n))
            row = ' '.join(row)
            if j >= i:
                res = 4 * n if i == j else 0
                result.append(f'(= {res} (+ {row}))')
    return '\n'.join(result)


def matrix_mult_element_expression(letter1, letter2, i, j, n):
    mults = []
    for k in range(n):
        mults.append(f'(* {letter1}_{i+1}_{k+1} {letter2}_{k+1}_{j+1})')
    mults = ' '.join(mults)
    return f'(+ {mults})'


if __name__ == '__main__':


    n = int(sys.argv[1])

    hadamard = \
        f"""
{declare_variables('A', n)}
{declare_variables('B', n)}
{declare_variables('C', n)}
{declare_variables('D', n)}

(assert (and
{value_constraints('A', n)}
{value_constraints('B', n)}
{value_constraints('C', n)}
{value_constraints('D', n)}

{circulant_matrix_constraints('A', n)}
{circulant_matrix_constraints('B', n)}
{circulant_matrix_constraints('C', n)}
{circulant_matrix_constraints('D', n)}

{symmetry_constraints('A', n)}
{symmetry_constraints('B', n)}
{symmetry_constraints('C', n)}
{symmetry_constraints('D', n)}

{sum_matrix_expression([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], n)}

))
(check-sat)
(get-model)
    """

    print(hadamard)
