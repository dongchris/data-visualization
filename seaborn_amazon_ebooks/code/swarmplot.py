import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="darkgrid",
	rc = {'figure.figsize':(11.7,8.27)})

publishers = pd.read_csv("publishers.csv")

np.random.seed(1)
publishers = publishers.sample(n=1500)

g = sns.swarmplot(x="type", y="gross sales", hue="type", data=publishers,
	palette = 'Set2')
g.axes.set_title("Gross Sales for Amazon E-books by Publisher Type\n", fontsize =25)

g.set_xlabel("\nType",fontsize=20)
g.set_ylabel("Gross Sales\n",fontsize=20)



g.figure.savefig("swarmplot.png")
plt.show()