# Example for studying
import matplotlib.pyplot as plt
import numpy as np

sports = ['Soccer', 'Basketball', 'Golf', 'Volleyball', 'Tennis']
playing_time = [35, 20, 45, 15, 30]
watching_time = [10, 15, 5, 20, 12]

x = np.arange(len(sports))  # positions for the groups
width = 0.35  # width of each bar

fig, ax = plt.subplots()
ax.bar(x - width/2, playing_time, width, label='Playing')
ax.bar(x + width/2, watching_time, width, label='Watching')

ax.set_ylabel('Time (minutes)')
ax.set_title('Abigail\'s Sports Activities')
ax.set_xticks(x)
ax.set_xticklabels(sports)
ax.legend()

plt.show()
