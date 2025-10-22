import matplotlib.pyplot as plt
import numpy as np

names = ['Brandon', 'Vanessa', 'Daniel', 'Kevin', 'William']
midterm = [85, 60, 60, 65, 100]
final = [90, 90, 65, 80, 95]

x = np.arange(len(names))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, midterm, width, label='Midterm')
ax.bar(x + width/2, final, width, label='Finals')

# Label and format
ax.set_ylabel('Score(points)')
ax.set_title('Scores on Midterm and Final Exams')
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.legend()

plt.show()

for item2, item3 in zip(midterm, final):
