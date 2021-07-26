import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors ").lower()
    computer = random.choice(['r', 'p', 's',])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You win'

    return 'You lose'

def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') | (player == 's' and opponent == 'p')\
        | (player == 'p' and opponent == 'r'):
        return True


print(play())