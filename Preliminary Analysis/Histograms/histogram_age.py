import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle('./dataframe')

plt.hist(df['dm005'], bins=50)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Age')
plt.show()