# A university surveyed its students about their opinions on campus housing.
# The following two-way table shows the responses from the 200 students
# who participated in the survey.
# Question: How many students in this sample had a
#  negative opinion of campus housing?

import pandas as pd

data = {
    'Male': [40, 36, 14],
    'Female': [42, 56, 12]
}

index = ['Positive Opinion', 'Negative Opinion', 'Neutral opinion']

table = pd.DataFrame(data, index=index)
print(table)

negative = table.loc['Negative Opinion'].sum()
print('Total amount of students that had negative opinion:', negative)
