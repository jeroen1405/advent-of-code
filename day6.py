from typing import List

def common_part(data, n):
    for line in data:
        for i in range(len(line) - n):
            sequence = line[i:i+n]
            if len(set(sequence)) == len(sequence):
                return i + n

def pt1(data: List[str]):
    return common_part(data, 4)

def pt2(data: List[str]):
    return common_part(data, 14)

