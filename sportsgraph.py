# Abigail loves sports! This weekend she spent time playing
# \[5\] sports.
# Create a bar graph to show how much time Abigail spent playing each sport.
# Soccer: 35 minutes
# Basketball: 20 minutes
# Golf: 45 minutes
# Volleyball: 15 minutes
# Tennis: 30 minutes


import matplotlib.pyplot as plt

sports = ['Soccer', 'Basketball', 'Golf', 'Volleyball', 'Tennis']
time = [35, 20, 45, 15, 30]
plt.bar(sports, time)
plt.ylabel('Time (min)')
plt.title('Sports played by Abigail')
plt.show()
