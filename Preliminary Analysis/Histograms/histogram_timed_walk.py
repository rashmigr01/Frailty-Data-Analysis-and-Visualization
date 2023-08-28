import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle('./dataframe')

columns_list = df.columns.values

#bm054 to bm058 are the variables concerning timed walk

columns_to_plot = ['bm056', 'bm057']
names = ['Timed walk - 1st test', 'Timed walk - 2nd test']

fig, axs = plt.subplots(1, 2, figsize=(10, 8))

axs = axs.flatten()

for i, column in enumerate(columns_to_plot):
    ax = axs[i]
    ax.hist(df[column], bins=50)
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {names[i]}')

plt.tight_layout()

plt.show()