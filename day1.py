import helpers
import numpy as np

def create_totals(content):
    totals = []
    total = 0
    for line in content:
        if line == '':
            totals.append(total)
            total = 0
        else:
            total += int(line)
    return totals

def pt1(content):
    totals = create_totals(content)
    return max(totals)

def pt2(content):
    totals = create_totals(content)
    sorted_totals = np.sort(totals)[::-1]
    top_3 = sorted_totals[0:3]
    return top_3.sum()