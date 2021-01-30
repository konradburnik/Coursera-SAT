"""

COURSERA Course: Automated Reasoning - Satisfiability

Honorary Assignment - Program Correctness
TOTAL POINTS 1

"""

import sys


def declare_vars():
    var_a = [f'(declare-const A{i} Int)' for i in range(11)]
    new_line = ['\n']
    var_b = [f'(declare-const B{i} Int)' for i in range(11)]
    return '\n'.join(var_a + new_line + var_b)


def specify_initial_state():
    return '(and (= A0 1) (= B0 1))'


def specify_transitions():
    steps = [
        f"""(or
              (and (= A{j} (+ A{j-1} (* 2 B{j-1}))) (= B{j} (+ B{j-1} {j})))
              (and (= B{j} (+ A{j - 1} B{j - 1})) (= A{j} (+ A{j-1} {j})))
            )
        """
        for j in range(1, 11)]
    return '\n'.join(steps)


def declare_final_condition(n):
    return f'(= B10 (+ 600 {n}))'


if __name__ == '__main__':
    n = int(sys.argv[1])
    program_check = \
        f"""
{declare_vars()}

(assert (and
 {specify_initial_state()}

 {specify_transitions()}

 {declare_final_condition(n)}
))
(check-sat)
(get-model)
    """

    print(program_check)
