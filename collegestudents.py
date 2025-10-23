# Researchers surveyed college students about their Facebook use.
# The following two-way table shows the responses from the students
# who participated in the survey.
# Question: How many students aged 18 to 22 reported that they use Facebook?

import pandas as pd

data = {
    'Uses Facebook': [78, 70],
    'Does not use Facebook': [70, 67]
}
index = ['18 to 22', '23+']
table = pd.DataFrame(data, index=index)
print(table)

students = table.loc['18 to 22', 'Uses Facebook']
print('Number of students from 18 to 22, who use Facebook:', students)
