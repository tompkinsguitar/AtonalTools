"""
author: Daniel C. Tompkins tompkinsguitar [at] gmail [dot] com
Returns interval-class vectors and pitch-class sets given a list of pitch integers
code made for a doctoral seminar by Clifton Callender: https://github.com/cliftoncallender
"""

def icv(list_of_pitches):
    """Returns the interval class vectors of pitch set"""
    pitch_classes = set(x % 12 for x in list_of_pitches)
    pitch_classes = list(pitch_classes)
    icv_dict = {x: 0 for x in range(1, 7)}
    for i in range(len(pitch_classes)-1):
        for j in range(i+1, len(pitch_classes)):
            x = pitch_classes[i]
            y = pitch_classes[j]
            # print(x, y)
            ic = min((abs(y - x), 12-abs(x - y))) #% 6
            # print(ic)
#             if ic in icv_dict.keys():
            if ic == 0:
                ic = 6
            icv_dict[ic] += 1
    # print(icv_dict)
    final_icv = []
    for x in range(1, 7):
        z = icv_dict[x]
        final_icv.append(z)
    return final_icv


def prime_form(pitches):
    """Returns prime form after attempting all inversions and transpositions of set"""
    pc_set = sorted(set([pitch % 12 for pitch in pitches]))
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




test_pitches = [0, 4, 2, 5, 3, 77] #works with numbers ove 12 and microtonal (nondiscrete) pitches
icv(test_pitches)

prime_form(test_pitches)
