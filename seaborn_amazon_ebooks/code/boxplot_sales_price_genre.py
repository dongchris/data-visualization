import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="darkgrid",
	rc = {'figure.figsize':(11.7,8.27)})

publishers = pd.read_csv("publishers.csv")

g = sns.boxplot(x = "genre", y = "sale price", data = publishers,
				palette = "Set1")
plt.title("Boxplot of Amazon E-books Sale Price by Genre")

g.axes.set_title("Boxplot of Amazon E-books Sale Price by Genre\n",fontsize=25)
g.set_xlabel("\nGenre",fontsize=20)
g.set_ylabel("Sale Price\n",fontsize=20)


g.figure.savefig("boxplot.png")
plt.show()