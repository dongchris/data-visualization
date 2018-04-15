import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="darkgrid",
	rc = {'figure.figsize':(20,20)})

publishers = pd.read_csv("publishers.csv")
subset = publishers[['average rating', 'genre', 'units sold']]
subset['average rating'] = np.round(subset['average rating'], 0)
subset = pd.pivot_table(subset, values = 'units sold',
				 index = 'genre', columns = 'average rating')
print subset

g = sns.heatmap(data = subset, cmap = 'YlGnBu')
plt.yticks(rotation = 0)


g.axes.set_title("Heat Map of Units Sold for Amazon E-books by Genre and Average Rating\n",
	fontsize = 25)

g.set_xlabel("\nAverage Rating",fontsize=20)
g.set_ylabel("Genre\n",fontsize=20)



g.figure.savefig("heatmap.png")

plt.show()