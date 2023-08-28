import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle('./dataframe')

columns_list = df.columns.values

#bm036 - bm053 are the variables concerned with balance test

fig, axs = plt.subplots(1, 2, figsize=(10, 8))
axs = axs.flatten()

ax = axs[0]
ax.hist(df['bm039'], bins=10) # Duration of balance test(semi-tandem)
ax.set_xlabel('Values')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram of Balance test(semi-tandem) duration')

ax = axs[1]
ax.hist(df['bm043'], bins=10) # Duration of balance test(side by side)
ax.set_xlabel('Values')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram of Balance test(side-by-side) duration')

plt.show()
