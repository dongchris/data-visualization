import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="darkgrid",
	rc = {'figure.figsize':(11.7,8.27)})

publishers = pd.read_csv("publishers.csv")

g = sns.stripplot(x = "genre", y = "author revenue", data = publishers, jitter = True)
g.axes.set_title("Author Revenue for Amazon E-books by Genre\n", fontsize =25)

g.set_xlabel("\nGenre",fontsize=20)
g.set_ylabel("Author Revenue\n",fontsize=20)



g.figure.savefig("scatter_bivar.png")
plt.show()