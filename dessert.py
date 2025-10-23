# Gonna create another chart and try to add guidelines now, and then answer the question itself.
import matplotlib.pyplot as plt
import numpy as np

x = ['Vanilla', 'Chocolate', 'Strawberry', 'Cookie Dough']
y = [175, 225, 75, 200]

plt.bar(x, y)

# will add horizontal guidelines
for line in range(0, max(y)+25, 25):
    plt.axhline(y=line, color='grey', linestyle='--', linewidth=0.5)

plt.ylabel('Number of Customers')
plt.xlabel('Ice Cream flavours')
plt.title('Favourite flavours')
plt.show()


# Question: After Dessert Zone made the graph, 25 people changed
# their vote from chocolate to strawberry.
y[1] -= 25
y[2] += 25

plt.bar(x, y)
for line in range(0, max(y)+25, 25):
    plt.axhline(y=line, color='grey', linestyle='--', linewidth=0.5)

plt.ylabel('Number of Customers')
plt.xlabel('Ice Cream flavours')
plt.title('Favourite flavours')
plt.show()

max_votes = max(y)
fave = []
for i, votes in enumerate(y):
    if votes == max_votes:
        fave.append(x[i])

print(f'The most favourite flavour(s): {fave}')
