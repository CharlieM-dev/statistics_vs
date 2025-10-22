# Ruby had a budget of up to
# \[\$75\] to spend. Ruby made a graph of the costs of the items she bought.
# How much money did Ruby have left from her budget?
# given that the ticket = 5
# household items = 2 tickets, toys = 1 tickets, food = 4 tickets, clothing = 6 tickets.
def how_much_left():
    total = 75
    ticket = 5
    user_input1 = float(
        input('How many tickets did Ruby spent on household items: '))
    household = user_input1 * ticket

    user_input2 = float(
        input('How many tickets did Ruby spent on toys: '))
    toys = user_input2 * ticket

    user_input3 = float(
        input('How many tickets did Ruby spent on food: '))
    food = user_input3 * ticket

    user_input4 = float(
        input('How many tickets did Ruby spent on clothing: '))
    clothing = user_input4 * ticket

    total_spent = sum([household, toys, food, clothing])
    left_after = total - total_spent
    print(f'After what Ruby has spend, she had ${left_after}.')


how_much_left()
