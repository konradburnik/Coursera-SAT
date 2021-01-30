"""

COURSERA Course: Automated Reasoning - Satisfiability

Honorary Assignment - Filling trucks for a magic factory
TOTAL POINTS 2

"""


def trucks(j):
    return [f'(* w{i} T{j}{i})' for i in range(1, 6)]


def joined_trucks(j):
    return ' '.join(trucks(j))


def capacity(j):
    return f'(<= (+ {joined_trucks(j)}) 8000)'


def pallete_trucks(j):
    return [f'T{j}{i}' for i in range(1, 6)]


def pallete_joined_trucks(j):
    return ' '.join(pallete_trucks(j))


def pallete_capacity(j):
    return f'(<= (+ {pallete_joined_trucks(j)}) 8)'


def const_trucks():
    line = []
    for i in range(8):
        for j in range(5):
            truck = f'T{i+1}{j+1}'
            line.append(f'(declare-const {truck} Int)')
    return '\n'.join(line)


def const_weights():
    line = []
    for j in range(5):
        weight_var = f'w{j+1}'
        line.append(f'(declare-const {weight_var} Int)')
    return '\n'.join(line)


def pallet_weights():
    line = []
    for j, w in enumerate([800, 1100, 1000, 2500, 200]):
        weight_var = f'w{j+1}'
        line.append(f'(= {weight_var} {w})')
    all_weights = '\n'.join(line)
    return f'(and {all_weights})'


def trucks_non_neg():
    line = []
    for i in range(8):
        for j in range(5):
            truck = f'T{i+1}{j+1}'
            line.append(f'(>= {truck} 0)')
    all_nonneg = '\n'.join(line)
    return f'(and {all_nonneg})'


def nuzzles_risk():
    line = []
    for i in range(8):
        truck = f'(<= T{i+1}{1} 1)'
        line.append(truck)
    all_trucks = '\n'.join(line)
    return f'(and {all_trucks})'


def capacity_trucks():
    cap_trucks = [capacity(j) for j in range(1, 9)]
    all_cap_trucks = '\n'.join(cap_trucks)
    return f'(and {all_cap_trucks})'


def pallete_capacity_trucks():
    cap_trucks = [pallete_capacity(j) for j in range(1, 9)]
    all_cap_trucks = '\n'.join(cap_trucks)
    return f'(and {all_cap_trucks})'


def truck_cooling():
    line = []
    for i in range(3, 8):
        truck = f'(= T{i+1}{3} 0)'
        line.append(truck)
    all_trucks = '\n'.join(line)
    return f'(and {all_trucks})'


def prittles_crottles_explosive():
    line = []
    for i in range(8):
        truck = f'(not (and (> T{i+1}{2} 0) (> T{i+1}{4} 0)))'
        line.append(truck)
    all_trucks = '\n'.join(line)
    return f'(and {all_trucks})'


def total(j, num_items):
    trucks = ' '.join([f'T{i+1}{j}' for i in range(8)])
    return f'(= (+ {trucks}) {num_items})'


def total_items_all():
    line = []
    for j, num in enumerate([4, 'P', 8, 10, 20]):
        line.append(total(j + 1, num))
    all_items = '\n'.join(line)
    return f'(and {all_items})'


def declare_target():
    return '(declare-const P Int)'


def constraint_target():
    return '(>= P 0)'


if __name__ == '__main__':
    phi = f"""
        {const_trucks()}
        {const_weights()}
        {declare_target()}
        (assert (and
        {pallet_weights()}
        {trucks_non_neg()}
        {nuzzles_risk()}
        {capacity_trucks()}
        {pallete_capacity_trucks()}
        {truck_cooling()}
        {total_items_all()}
        {prittles_crottles_explosive()}
        {constraint_target()}
        ))
        (maximize P)
        (check-sat)
        (get-model)
    """
    print(phi)
