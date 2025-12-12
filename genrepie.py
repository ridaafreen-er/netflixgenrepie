import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\ADMIN\Downloads\movie_genre_dataset_big.csv")
gen_counts=df['genre'].value_counts()
x=gen_counts.index
y=gen_counts.values
plt.figure(figsize=(7,7))
plt.pie(y, labels=x)
plt.title("Movie Genre Distribution")
plt.show()