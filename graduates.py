# Researchers surveyed recent graduates of
# two different universities about their income.
# The following two-way table displays data for the sample of
#  graduates who responded to the survey.
# How many graduates in the sample had an income of
# \$40000 and over?

import pandas as pd

data = {
    'University A': [35, 90, 35],
    'University B': [40, 63, 37]
}

index = ['Under $20,000', '$20,000 to $39,999', '$40,000 and over']
table = pd.DataFrame(data, index=index)
print(table)

# Now we are going to be looking for total amount of grads
# who had more than 40 grand
total_40000 = table.loc['$40,000 and over'].sum()
print('Total graduates with $40,000 and over:', total_40000)
