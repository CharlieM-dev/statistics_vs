# I need to create a pictograph with the recycling data
# given that one symbol = 3 kg of garbage
# paper = 8 symbols
# glass = 2 symbols
# plastic = 4 symbols
# aluminium = 6 symbols
import matplotlib.pyplot as plt

values_of_recycling = []
num_symbols = [8, 2, 4, 6]
types_of_recycling = ['Paper', 'Glass', 'Plastic', 'Aluminium']
symbol = '♻️'

padding = 1           # empty cells on left/right
symbol_size = 30      # fontsize
fig_width_per_symbol = 0.6

# Figure width proportional to max symbols + padding
fig_width = max(num_symbols) * fig_width_per_symbol + 2*padding
fig_height = len(types_of_recycling)  # one unit per row
fig, ax = plt.subplots(figsize=(fig_width, fig_height))

# Place symbols
for i, (recycling_type, symbol_count) in enumerate(zip(types_of_recycling, num_symbols)):
    for j in range(symbol_count):
        ax.text(j + padding, i, symbol, fontsize=symbol_size,
                ha='center', va='center')

# Formatting
ax.set_yticks(range(len(types_of_recycling)))
ax.set_yticklabels(types_of_recycling, fontsize=12)
ax.set_xticks([])

# Set x-limits with padding
ax.set_xlim(0, max(num_symbols) + 2*padding)
ax.set_ylim(-0.5, len(types_of_recycling)-0.5)  # gives vertical padding

ax.set_title('The recycling amounts', fontsize=16,
             pad=20)  # pad moves it above symbols

plt.tight_layout()  # ensures title and symbols don't overlap
plt.show()

scale = 3

for i in num_symbols:
    kg = i * scale
    values_of_recycling.append(kg)

print(f'The amount of kilograms of recycling is: {values_of_recycling}')
# The qustions itself is:

# How many kilograms of recycling have been brought to the drive in all?
total_kilograms = sum(values_of_recycling)
print(
    f'The total amount of kilograms of recycling that have been brought to the drive is: {total_kilograms}')
