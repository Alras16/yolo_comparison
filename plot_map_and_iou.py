import matplotlib.pyplot as plt
import numpy as np
import os
import sys

fn = sys.argv[1]
#if os.path.exists(fn):
#    print os.path.basename(fn)

with open(fn, 'r') as data:
    x = []
    y = []
    z = []
    v = []
    for line in data:
        p = line.split(',')
        x.append(int(p[0]))
        y.append(float(p[1]))
        z.append(float(p[2]))
        v.append(float(p[3]))

plt.figure(figsize=(7,5))
axes = plt.gca()
axes.set_ylim([-0.005,100])
axes.set_xlim([-0.005,2600])
plt.rcParams.update({'font.size': 27})
plt.style.use('seaborn-bright') # seaborn-bright
plt.plot(x, y, color="gold", linewidth=3)
plt.plot(x, z, color="blue", linewidth=3)
plt.plot(x, v, color="green", linewidth=3)
plt.legend(["320 x 320", "416 x 416", "608 x 608"], fontsize=15)
plt.ylabel('Avg. IoU', fontsize = 20)
plt.xlabel('Iteration', fontsize = 20)
plt.grid(True)
plt.tight_layout()
plt.savefig("random.png")
plt.show()