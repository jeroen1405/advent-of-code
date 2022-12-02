import helpers
import numpy as np

content = helpers.load_txt_file(1)
totals = []
total = 0
for line in content:
    if line == '\n':
        totals.append(total)
        total = 0
    else:
        total += int(line)

print(max(totals))

sorted_totals = np.sort(totals)[::-1]
top_3 = sorted_totals[0:3]
print(top_3.sum())