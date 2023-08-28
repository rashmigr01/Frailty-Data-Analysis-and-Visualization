import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle('./dataframe')

plt.figure(figsize=(8, 6))
plt.scatter(df['bm029'], df['bm039'], alpha=0.5)
plt.xlabel('bm029')
plt.ylabel('bm039')
plt.title('Scatter Plot of Grip test vs Balance test')
plt.grid(True)

print(df[df['bm026'] == '1'].shape[0])
plt.show()





