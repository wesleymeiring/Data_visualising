import numpy as np
import matplotlib.pyplot as plt

# Imports csv file
galaxy = np.genfromtxt('graph_data\InaGalaxyFarAway.csv', dtype="str", delimiter=',')  # import InaGalaxyFarAway file
dic = {"Fantasia": "r", "Utopia": "b", "Barsoom": "y", "Westeros": "g"}  # assigns colours to each continent

n = galaxy[1:, 1].astype("float")  # pulls data of population
area = n ** 0.25  # determines size of bubble

x = galaxy[1:, 2].astype("float")  # pulls data of GDP per capita
y = galaxy[1:, 3].astype("float")  # pulls data of life expectancy
continents = galaxy[1:, 0]  # pulls name of continents
colours = []
for c in continents:  # appends colours to each continent as it loops through list
    colours.append(dic[c])

# Design Scatter plot graph
plt.scatter(x, y, s=area, c=colours, cmap="jet")
plt.title("Scatter plot representing GDP vs life expentancy and includes population size")
plt.xlabel("GDP per capita")
plt.ylabel("Life expectancy")

plt.show()
