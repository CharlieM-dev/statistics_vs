import pandas as pd

data = {
    'AFC': [7, 9],
    'NFC': [8, 8]
}

index = ['Animal', 'Non-animal']

# Creating a table

table = pd.DataFrame(data, index=index)
print(table)

# How many teams are in NFC?
nfc_total = table['NFC'].sum()
print(f'In total NFC has this many teams: {nfc_total}')
