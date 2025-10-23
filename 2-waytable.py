import pandas as pd

data = {
    'AFC': [7, 9],
    'NFC': [8, 8]
}

index = ['Animal', 'Non-animal']

# Creating a table

table = pd.DataFrame(data, index=index)
print(table)
