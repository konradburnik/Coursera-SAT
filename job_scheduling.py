"""

COURSERA Course: Automated Reasoning - Satisfiability

Honorary Assignment - Job Scheduling
TOTAL POINTS 3

"""


def declare_task_runtimes():
    start_times = [f'(declare-const S{i+1} Int)' for i in range(10)]
    end_times = [f'(declare-const E{i+1} Int)' for i in range(10)]
    return '\n'.join(start_times) + '\n\n'.join(end_times)


def declare_total_running_time():
    return f'(declare-const T Int)'


def start_times_end_times_constraints():
    return '\n'.join([
        f'(and (>= S{i+1} 0) (<= E{i+1} T))' for i in range(10)])


def task_runtimes_constraints():
    return '\n'.join([
        f'(= E{i+1} (+ S{i+1} (+ 10 {i+1})))' for i in range(10)])


def base_constraints():
    predecessors = {
        1: [],
        2: [],
        3: [1, 2],
        4: [],
        5: [],
        6: [2, 4],
        7: [1, 4, 5],
        8: [3, 6],
        9: [6, 7],
        10: [8, 9]
    }
    cons = []
    for task, pred in predecessors.items():
        for prev_task in pred:
            cons.append(f'(>= S{task} E{prev_task})')
    return '\n'.join(cons)


def special_constraint_1():
    return '(>= S7 S8)'


def not_at_same_time(i, j):
    return f'(or (>= S{i} E{j}) (>= S{j} E{i}))'


def special_constraint_2():
    return f"""(and
      {not_at_same_time(3, 4)}
      {not_at_same_time(4, 5)}
      {not_at_same_time(3, 5)}
    )"""


if __name__ == '__main__':
    scheduling = \
        f"""
{declare_task_runtimes()}

{declare_total_running_time()}

(assert (and
 {start_times_end_times_constraints()}

 {task_runtimes_constraints()}

 {base_constraints()}

))
(minimize T)
(check-sat)
(get-model)
    """

    print(scheduling)
