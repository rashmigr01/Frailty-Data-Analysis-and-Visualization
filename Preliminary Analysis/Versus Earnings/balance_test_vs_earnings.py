import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle('./dataframe')

plt.figure(figsize=(8, 6))
plt.scatter(df['bm039'], df['we020_i'], alpha=0.5)
plt.xlabel('bm039')
plt.ylabel('we020_i')
plt.title('Scatter Plot of Balance Test vs Weekly earnings')
plt.grid(True)

plt.show()