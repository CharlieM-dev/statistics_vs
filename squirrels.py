total = 80
acorn = 4
ground_squirrels = acorn * 5.5
print(f'Ground squirrels are {ground_squirrels} acorns.')

flying_squirrels = acorn * 2
print(f'Flying squirrels ate {flying_squirrels} acorns.')

fox_squirrels = acorn * 6
print(f'Fox squirrels ate {fox_squirrels} acorns.')

gray_squirrels = acorn * 2.5
print(f'Gray squirrels ate {gray_squirrels} acorns.')

total_ate = ground_squirrels + flying_squirrels + fox_squirrels + gray_squirrels
print(f'In total squirrels ate {total_ate}')

left_after_ate = total - \
    (ground_squirrels + flying_squirrels + fox_squirrels + gray_squirrels)
print(f'After all squirrels ate, Nancy had {left_after_ate} acorns')

# Gonna try to make a function


def total_left():
    total_acorns = 80
    a = 4
    user_input1 = float(
        input('Please, tell us how many acorns ground squirrels ate: '))
    ground = user_input1

    user_input2 = float(
        input('Please, tell us how many acorns flying squirrels ate: '))
    flying = user_input2

    user_input3 = float(
        input('Please, tell us how many acorns fox squirrels ate: '))
    fox = user_input3

    user_input4 = float(
        input('Please, tell us how many acorns gray squirrels ate: '))
    gray = user_input4

    ground_ate = ground * a

    flying_ate = flying * a

    fox_ate = fox * a

    gray_ate = gray * a

    total_eaten = sum([ground_ate, flying_ate, fox_ate, gray_ate])
    print(f'All the squirrels ate {total_eaten}')
    left = total_acorns - total_eaten
    print(
        f'After the squirrels had their mighty fest, Nancy was left with {left} acorns')


total_left()
