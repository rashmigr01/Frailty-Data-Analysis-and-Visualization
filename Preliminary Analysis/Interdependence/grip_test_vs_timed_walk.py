import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle('./dataframe')

plt.figure(figsize=(8, 6))
plt.scatter(df['bm029'], df['bm056'], alpha=0.5)
plt.xlabel('bm029')
plt.ylabel('bm056')
plt.title('Scatter Plot of Grip test vs Timed Walk')
plt.grid(True)

plt.show()





