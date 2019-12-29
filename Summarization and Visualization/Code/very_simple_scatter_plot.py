# import matplotlib.pyplot as plt
# from collections import Counter
#
# x = [0, 1, 1, 2, 2, 2, 2, 2]
# y = [0, 1, 2, 3, 3, 3, 3, 5]
#
# c = Counter(zip(x, y))
# # create a list of the sizes, here multiplied by 10 for scale
# s = [10 * c[(xx, yy)] for xx, yy in zip(x, y)]
#
# plt.scatter(x, y, s=s)
# plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.normal(10,1,30).reshape(10,3),
                  index = pd.date_range('2010-01-01', freq = 'M', periods = 10),
                  columns = ('one', 'two', 'three'))
df['key1'] = (4,4,4,6,6,6,8,8,8,8)


fig, ax = plt.subplots()
sc = ax.scatter(df['one'], df['two'], marker = 'o', c = df['key1'], alpha = 0.8)
#ax.legend(*sc.legend_elements())
plt.show()