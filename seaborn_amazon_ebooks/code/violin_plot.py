import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="darkgrid",
	rc = {'figure.figsize':(11.7,8.27)})

publishers = pd.read_csv("publishers.csv")

g = sns.violinplot(x = "type", y = "sale price", data = publishers)

g.axes.set_title("Violin plot of Amazon E-books Sale Price by Type\n", fontsize =25)

g.set_xlabel("\nType",fontsize=20)
g.set_ylabel("Sales Price\n",fontsize=20)



g.figure.savefig("violinplot.png")

plt.show()