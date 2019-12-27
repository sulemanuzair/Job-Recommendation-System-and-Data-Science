import matplotlib.pyplot as plt
import pandas as pd

data = {'Low': 2, 'Medium': 4, 'High': 5}
df = pd.Series(data)

plt.bar(range(len(df)), df.values, align='center')
plt.xticks(range(len(df)), df.index.values, size='small')
plt.show()
