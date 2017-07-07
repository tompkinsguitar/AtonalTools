"""
author: Daniel C. Tompkins tompkinsguitar [at] gmail [dot] com
Produces sum-class tables from Joseph N. Straus (forthcoming)
"""

import itertools as it
import csv


cardinality = 3
all_permutations = it.combinations_with_replacement(range(12), cardinality)

def sum_class(pitches):
    pc_set = sorted([pitch % 12 for pitch in pitches])
    all_permutations = []

    def inversions(pcset, index):
        i_pitches = [(index - pc) % 12 for pc in pcset]
        return i_pitches

    def transpositions(pcset, index):
        t_pitches = [(index + pc) % 12 for pc in pcset]
        return t_pitches

    for x in range(12):
        all_permutations.append(sorted(inversions(pc_set, x)))
        all_permutations.append(sorted(transpositions(pc_set, x)))

    return min(all_permutations)

all_sum_classes = []

for sc in all_permutations:
    if sum_class(sc) not in all_sum_classes:
        all_sum_classes.append(sum_class(sc))

all_sum_classes = sorted(all_sum_classes)

header_row = ['']+[x for x in range(12)]
sc_table = [header_row]
for sc in all_sum_classes:
    sc_row = [tuple(sc)]
    for s in range(12):
        all_scs = []
        for n in range(12):
            test_sc = [(n+x)%12 for x in sc]
            if sum(test_sc)%12 == s and sorted(test_sc) not in all_scs:
                all_scs.append(sorted(test_sc))
        sc_row.append(all_scs)
    sc_table.append(sc_row)


def csv_function(f_variable, path):
        with open(path, 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(f_variable)


csv_function(sc_table, '%s.csv' %cardinality)


