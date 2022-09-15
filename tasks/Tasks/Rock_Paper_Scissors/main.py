import random

def rock_paper_scissors():

    amount_of_plays = int(input('How many plays? '))

    plays = {
        'P': 'paper',
        'S': 'scissors',
        'R': 'rock'
    }

    plays_list = []

    for i in range(amount_of_plays):
        player1 = random.choice(list(plays.values()))
        player2 = random.choice(list(plays.values()))
        plays_list.append([player1,player2])

    for play in plays_list:
        print('-'*10)
        print(f"Play: {(str(play[0]+' '+play[1]))}")
        p1 = play[0]
        p2 = play[1]

        # Tie
        if p1 == 'rock' and p2 == 'rock':
            print('Tie!')
        elif p1 == 'paper' and p2 == 'paper':
            print('Tie!')
        elif p1 == 'scissors' and p2 == 'scissors':
            print('Tie!')
        # P1 Wins
        elif p1 == 'rock' and p2 == 'scissors':
            print('Player1 Wins!')
        elif p1 == 'scissors' and p2 == 'paper':
            print('Player1 Wins!')
        elif p1 == 'paper' and p2 == 'rock':
            print('Player1 Wins!')
        # P2 Wins
        elif p2 == 'rock' and p1 == 'scissors':
            print('Player2 Wins!')
        elif p2 == 'scissors' and p1 == 'paper':
            print('Player2 Wins!')
        elif p2 == 'paper' and p1 == 'rock':
            print('Player2 Wins!')
    
    print()
    return 'Done!'
pass

print(rock_paper_scissors())