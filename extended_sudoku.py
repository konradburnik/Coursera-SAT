"""

COURSERA Course: Automated Reasoning - Satisfiability

Honorary Assignment - A Sudoku variant
TOTAL POINTS 1

"""


def declare_vars():
    list = []
    for i in range(9):
        for j in range(9):
            list.append(f'(declare-const X{i+1}{j+1} Int)')
    return '\n'.join(list)


def constraint_vals():
    list = []
    for i in range(9):
        for j in range(9):
            list.append(f'(and (>= X{i+1}{j+1} 1) (<= X{i+1}{j+1} 9))')
    return '\n'.join(list)


def distinct_row(i):
    vars = ' '.join([f'X{i+1}{j+1}' for j in range(9)])
    return f'(distinct {vars})'


def distinct_rows():
    rows = '\n'.join([distinct_row(i) for i in range(9)])
    return f'(and {rows})'


def distinct_col(j):
    vars = ' '.join([f'X{i+1}{j+1}' for i in range(9)])
    return f'(distinct {vars})'


def distinct_cols():
    cols = '\n'.join([distinct_col(j) for j in range(9)])
    return f'(and {cols})'


def distinct_block(x, y):
    return f"""(distinct
          X{x-1}{y-1} X{x}{y-1} X{x+1}{y-1}
          X{x-1}{y} X{x}{y} X{x+1}{y}
          X{x-1}{y+1} X{x}{y+1} X{x+1}{y+1}
    )"""


def distinct_blocks():
    line = []
    for x in [2, 5, 8]:
        for y in [2, 5, 8]:
            line.append(distinct_block(x, y))
    lines = '\n'.join(line)
    return f'(and {lines})'


def less_than_constraint():
    return """(and (< X24 X25) (< X25 X26) (< X26 X27) (< X27 X28) (< X28 X29)
(< X41 X42) (< X42 X43) (< X43 X44) (< X44 X45) (< X45 X46)
(< X64 X65) (< X65 X66) (< X66 X67) (< X67 X68) (< X68 X69)
(< X81 X82) (< X82 X83) (< X83 X84) (< X84 X45) (< X85 X86)
)"""


def diff_by_one_constraint():
    return """(and
(= (abs (- X12 X13)) 1)
(= (abs (- X14 X15)) 1)
(= (abs (- X17 X18)) 1)

(= (abs (- X32 X33)) 1)
(= (abs (- X34 X35)) 1)
(= (abs (- X35 X36)) 1)

(= (abs (- X51 X52)) 1)
(= (abs (- X52 X53)) 1)
(= (abs (- X54 X55)) 1)
(= (abs (- X56 X57)) 1)
(= (abs (- X58 X59)) 1)

(= (abs (- X63 X64)) 1)
(= (abs (- X73 X74)) 1)
(= (abs (- X86 X87)) 1)

(= (abs (- X43 X53)) 1)
(= (abs (- X63 X73)) 1)

(= (abs (- X16 X26)) 1)
(= (abs (- X66 X76)) 1)

(= (abs (- X27 X37)) 1)
(= (abs (- X37 X47)) 1)
(= (abs (- X47 X57)) 1)
(= (abs (- X67 X77)) 1)

(= (abs (- X39 X49)) 1)
(= (abs (- X49 X59)) 1)
)
"""

if __name__ == '__main__':
    phi = f"""{declare_vars()}

(assert (and
{constraint_vals()}

{distinct_rows()}

{distinct_cols()}

{distinct_blocks()}

{less_than_constraint()}

{diff_by_one_constraint()}
))
(check-sat)
(get-model)
    """
    print(phi)
