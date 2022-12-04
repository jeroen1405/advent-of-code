from typing import List
import numpy as np

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

def pt1(data: List[str]):
    total_contained = 0
    for line in data:
        elf_ranges = line.split(',')
        # total_shifts = []
        elves = {}
        for i, elf in enumerate(elf_ranges):
            start, end = elf.split('-')
            elves[i] = [j for j in range(int(start), int(end) + 1)]
        if sublist(elves[0], elves[1]):
            total_contained += 1
        elif sublist(elves[1], elves[0]):
            total_contained += 1
    return total_contained

def pt2(data: List[str]):
    total_overlap = 0
    for line in data:
        elf_ranges = line.split(',')
        total_shifts = []
        elves = {}
        for i, elf in enumerate(elf_ranges):
            start, end = elf.split('-')
            elves[i] = [j for j in range(int(start), int(end) + 1)]
            total_shifts += elves[i]
        u, c = np.unique(total_shifts, return_counts=True)
        dup = u[c > 1]
        if len(dup) > 0:
            total_overlap += 1
    return total_overlap
