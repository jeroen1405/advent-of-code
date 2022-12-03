def char_to_priority(char):
    # ASCII table: A = 65, a = 97
    # convert to ASCII value, set array to start at 0 and
    # add AoC priority (1-26 for lowercase, 27-52 for uppercase)
    if char.islower():
        prio = ord(char) - 97 + 1
    else:
        prio = ord(char) - 65 + 27
    return prio

def pt1(data):
    total_priority = 0
    for line in data:
        n = len(line)
        assert n % 2 == 0
        cpt1, cpt2 = line[:int(n/2)], line[int(n/2):]
        common = None
        for char in cpt1:
            if char in cpt2:
                common = char
                break
        prio = char_to_priority(common)
        total_priority += prio
    return total_priority

def pt2(data):
    groups = []
    group = []
    for i, line in enumerate(data):
        if i % 3 == 0 and i != 0:
            groups.append(group)
            group = []
        group.append(line)
    groups.append(group)

    total_priority = 0
    for elf1, elf2, elf3 in groups:
        common = None
        for char in elf1:
            if (char in elf2) & (char in elf3):
                common = char
                break
        prio = char_to_priority(common)
        total_priority += prio
    return total_priority