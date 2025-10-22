import matplotlib.pyplot as plt

items = ['Household', 'Toys', 'Food', 'Clothing']
costs = [10, 5, 20, 30]  # example from Ruby

plt.bar(items, costs)
plt.ylabel('Cost ($)')
plt.title('Ruby’s Expenses')
plt.show()
