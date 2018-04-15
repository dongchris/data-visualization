import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="darkgrid",
	rc = {'figure.figsize':(11.7,8.27)})

publishers = pd.read_csv("publishers.csv")

g = sns.barplot(x = "genre", y = "units sold", data = publishers,
				palette = "Set1")

g.axes.set_title("Average Units Sold for Amazon E-books by Genre\n",fontsize=25)
g.set_xlabel("\nGenre",fontsize=20)
g.set_ylabel("Units Sold\n",fontsize=20)

g.figure.savefig("barplot_books_sold_genre.png")
plt.show()