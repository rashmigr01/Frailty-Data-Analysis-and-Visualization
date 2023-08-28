import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle('./dataframe')

columns_list = df.columns.values

#bm024 to bm034 are concerned variables of grip test denoting history, range of efforts, dominant hand etc

columns_to_plot = ['bm029', 'bm031', 'bm028', 'bm030']
names = ['Right arm grip - 1st test', 'Right arm grip - 2nd test', 'Left arm grip - 1st test', 'Left arm grip - 2nd test']

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs = axs.flatten()

for i, column in enumerate(columns_to_plot):
    ax = axs[i]
    ax.hist(df[column], bins=10)
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {names[i]}')

plt.tight_layout()

plt.show()
