import random

plays = {
    2: 'paper',
    4: 'scissors',
    6: 'rock'
}

print(random.choice(list(plays.values())))