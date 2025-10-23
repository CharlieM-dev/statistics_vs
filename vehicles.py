import matplotlib.pyplot as plt
import numpy as np
import statistics as st
# Motorcycles 17
# Convertibles 13
# Garbage trucks 4
# Bulldozers 9

number_built = [17, 13, 4, 9]
vehicle_type = ['Motorcycle', 'Convertibles', 'Garbage trucks', 'Bulldozers']

# barh is short for bar horizontal and it will make bars to come from the left,

plt.barh(vehicle_type, number_built, height=0.4)

# whilst bar will by defult make them come from down to up
plt.ylabel('Vehicle Type')
plt.xlabel('Number built')
plt.title('Number of Vehicles built')
plt.show()

# How many fewer bulldozers were built than garbage trucks and motorcycles combined?
garbage_motorcycles_comb = number_built[0] + number_built[2]
print(
    f'The garbage trucks and motorcycles combines are: {garbage_motorcycles_comb}.')
difference = garbage_motorcycles_comb - number_built[3]
print(f'There were {difference} trucks and motorcycles more than bulldozers.')
