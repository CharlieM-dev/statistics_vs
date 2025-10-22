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
    result = item2 - item3
    print(
        f'With the midterm score{item2}, and final exam score {item3}, we get such a score as a difference: {result}')


for m, f in zip(midterm, final):
    result = f - m
    print(f'Midterm: {midterm}. Final: {final}. Difference: {result}')

improved = []
for n, m, f in zip(names, midterm, final):
    if f > m:
        improved.append(names)

print(f"\nStudents who improved their scores: {improved}")
