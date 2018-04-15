import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="darkgrid",
	rc = {'figure.figsize':(11.7,8.27)})

publishers = pd.read_csv("publishers.csv")

publishers = publishers[publishers['type']!='amazon']
publishers = publishers[publishers['genre']!='comics']
publishers = publishers[publishers['genre']!='foreign language']

g = sns.FacetGrid(publishers, row="genre", col="type", margin_titles=True)

g.set(xticks = np.arange(0,6,1))
	
g.map(plt.hist, "average rating", color="#2ecc71", bins = 5)

plt.subplots_adjust(top = 0.9, hspace = 0.4)
g.fig.suptitle('Histogram of Average Rating by Genre and Type')


g.savefig("facet_histogram.png")
plt.show() 