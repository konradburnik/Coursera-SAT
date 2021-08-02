import sys

"""

 Hadamard Matrix Finder - not course related

"""


def declare_variables(letter, n):
    vars = [
        f'(declare-const {letter}_{i+1}_{j+1} Int)' for i in range(n) for j in range(n) if j >= i]
    return '\n'.join(vars)


def value_constraints(letter, n):
    cons = [f'(or (= {letter}_{i+1}_{j+1} 1) (= {letter}_{i+1}_{j+1} -1))' for i in range(n)
            for j in range(n) if j >= i]
    return '\n'.join(cons)


def circulant_matrix_constraints(letter, n):
    circulant = [
        f'(= {letter}_{i+1}_{j+1} {letter}_{1}_{(j-i) % n + 1})' for i in range(1, n) for j in range(n) if j >= i]
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
        ii = i; kk1 = k; kk2 = k; jj = j;
        if kk1 < ii: ii, kk1 = kk1, ii
        if kk2 > jj: jj, kk2 = kk2, jj
        mults.append(f'(* {letter1}_{ii+1}_{kk1+1} {letter2}_{kk2+1}_{jj+1})')
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


{sum_matrix_expression([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], n)}

))
(check-sat)
(get-model)
    """

    print(hadamard)
