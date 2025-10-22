# Olivia counted the number of ladybugs on each plant in her garden, then made the graph below.
# If \[10\] ladybugs fly from the lettuce to the alfalfa, which
# \[2\] kinds of plants will have the same number of ladybugs?
# given bug = 5, roses = 7 bugs, lettuce = 3 bugs, alfalfa = 5 bugs, grape vines = 2 bugs
def kinds_of_plants():
    bug = 5
    plants = {
        "roses": 7 * bug,
        "lettuce": 3 * bug,
        "alfalfa": 5 * bug,
        "grape_vines": 2 * bug
    }

    print("At the start:")
    for plant, count in plants.items():
        print(f"{plant.capitalize()}: {count} ladybugs")

    # Migration: 10 ladybugs from lettuce to alfalfa
    plants["lettuce"] -= 10
    plants["alfalfa"] += 10

    print("\nAfter migration:")
    for plant, count in plants.items():
        print(f"{plant.capitalize()}: {count} ladybugs")

    # Find which plants have the same number of ladybugs
    counts_seen = {}
    for plant, count in plants.items():
        if count in counts_seen:
            print(
                f"{plant.capitalize()} and {counts_seen[count]} have the same number of ladybugs!")
        else:
            counts_seen[count] = plant


kinds_of_plants()
