import numpy as np
import matplotlib.pyplot as plt

b = map(int,open('data/dist_distances_enfermos_same_chr').readlines())
a = map(int,open('data/dist_distances_sanos_same_chr').readlines())

plt.hist(b, bins=100, normed=0, alpha=0.5, label='enfermos')
plt.hist(a, bins=100, normed=0, alpha=0.5, label='sanos')
plt.legend(loc='upper right')

plt.show()
