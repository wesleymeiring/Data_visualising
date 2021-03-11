import numpy as np
import matplotlib.pyplot as plt

# Create a pie graph for monthly expenses

# Imports txt File
cost = np.loadtxt("graph_data\costs_too.txt", dtype='str', delimiter=',')
# Puts float data in array
costs = cost[1:, 2:].astype("float")
# Puts names of months which are strings in arrays
month_names = cost[1:, 1].astype("str")
# Sums up the total of each months expenses
total_monthly_cost = np.sum(costs, axis=1)

# Size of pie graph
fig = plt.figure(figsize=(10, 10))
# Figures that need to go into pie graph
plt.pie(total_monthly_cost, labels=month_names, autopct='%1.1f%%')
plt.title("Break down monthly total expenditure")

category_names = cost[0, 2:].astype("str")
total_category_cost = np.sum(costs, axis=0)

plt.figure(figsize=(10, 10))
# Figures that need to go into pie graph
plt.pie(total_category_cost, labels=category_names, autopct='%1.1f%%')
plt.title("Break down total expenditure per category")

plt.show()
