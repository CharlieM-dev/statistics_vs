# What's the median score for final exam
# What's the midrange of the midterm score
# The average student score for the final exam
# What was the mode for the final exam scores
# What is the range of the midterm scores

# 1. We need to create a graph itself
import matplotlib.pyplot as plt
import numpy as np
import statistics as st

name = ['Ishaan', 'Emily', 'Daniel', 'Jessica', 'William']
midterm = [90, 90, 60, 100, 80]
final = [100, 100, 100, 75, 80]

x = np.arange(len(name))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, midterm, width, label='Midterm')
ax.bar(x + width/2, final, width, label='Final')

# No we need to label and format our table and bars
ax.set_ylabel('Score (points)')  # Label of vertical coordinates of the graph
ax.set_title('Scores on Midterm and Final exams')
# gives horizontal coordinates actual names not just a bunch of numbers
ax.set_xticks(x)
ax.set_xticklabels(name)
ax.legend()  # shows us the legend of the chart
plt.show()  # finally shows us the chart itself
# Now we can get to perform operations on the grah itself.
# What's the median score for final exam
# For that operation we can import statistics module
median_final = st.median(final)
print(f'The median for final exams score is: {median_final}')


# What's the midrange of the midterm score
midrange_midterm = (min(midterm) + max(midterm)) / 2
print(f'The midrange for midterm exam scores is: {midrange_midterm}')

# The average student score for the final exam
# but you can also do: final_average = statistics.mean(final)
final_average = sum(final) / len(final)
print(f'The average for the final exam scores is: {final_average}')

# What was the mode for the final exam scores
final_mode = st.mode(final)
print(f'The mode for the final exam results is: {final_mode}')

# What is the range of the midterm scores
range_midterm = max(midterm) - min(midterm)
print(f'The range of midterm result scores is: {range_midterm}')
