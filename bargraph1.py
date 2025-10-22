# On a family road trip, Ivy is playing a game where she counts the number of different-colored cars that drive past.
# Create a bar graph to show how many cars of each color passed Ivy's family's car.
# Red cars
# \[12\]
# Blue cars
# \[20\]
# Silver cars
# \[12\]
# Black cars
# \[16\]
# Green cars
# \[4\]

import matplotlib.pyplot as plt
cars = ['Red cars', 'Blue cars', 'Silver cars', 'Black cars', 'Green cars']
number = [12, 20, 12, 16, 4]
plt.bar(cars, number)
plt.ylabel('Number of cars')
plt.title('Color of cars')
plt.show()
