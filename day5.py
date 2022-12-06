from typing import List

def parse_input(data):
    commands = []
    crates = []
    configuration = {}
    for line in data:
        if 'move' in line:
            commands.append(line)
        elif '1' in line:
            keys = line.split()
            for key in keys:
                configuration[int(key)] = []
        else:
            # Configuration is defined after crates so store crates
            # in temporary list before parsing
            crates.append(line)

    for line in crates:
        for i, char in enumerate(line):
            # Use the fact that every set of four characters corresponds
            # to one configuration key to find out what letter corresponds
            # to what key
            if char.isalnum(): # isalnum() checks for alphabet or number
                # character occurs at index 1 + 4n, solve for n to put in right list
                # also array starts at 1
                key = int((i - 1) / 4) + 1
                configuration[key].append(char)

    # Sort crate configuration to put top crate at the end of list
    for key, crate_order in configuration.items():
        configuration[key] = crate_order[::-1]
    return commands, configuration

def pt1(data: List[str]):
    commands, configuration = parse_input(data)
    for command_line in commands:
        splits = command_line.split()
        amount, origin, destination = [int(i) for i in splits[1:6:2]]
        for _ in range(amount):
            crate = configuration[origin].pop()
            configuration[destination].append(crate)

    top_crates = ''
    for stack in configuration.values():
        top_crates += stack[-1]
    return top_crates


def pt2(data: List[str]):
    commands, configuration = parse_input(data)
    for command_line in commands:
        splits = command_line.split()
        amount, origin, destination = [int(i) for i in splits[1:6:2]]
        crates = configuration[origin][-amount:]
        configuration[origin] = configuration[origin][:-amount]
        configuration[destination].extend(crates)

    top_crates = ''
    for stack in configuration.values():
        top_crates += stack[-1]
    return top_crates
