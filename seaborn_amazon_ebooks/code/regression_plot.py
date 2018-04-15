import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="darkgrid",
	rc = {'figure.figsize':(11.7,8.27)})

publishers = pd.read_csv("publishers.csv")

g = sns.regplot(x = "author revenue", y = 'amazon revenue', data = publishers,
				color = '#e74c3c')

g.axes.set_title("Regression plot of Author vs Amazon Revenue\n",fontsize=25)

g.set_xlabel("\nAuthor Revenue",fontsize=20)
g.set_ylabel("Amazon Revenue\n",fontsize=20)



g.figure.savefig("regression.png")

plt.show()