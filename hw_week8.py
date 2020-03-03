import random

def hw_week8():
    print('ROCK, PAPER, SCISSORS')
    w = 0   #win
    l = 0   #losses
    t = 0   #Ties
    while True:
        print(str(w) + ' Wins, ' + str(l) + ' Losses, ' + str(t) + ' Ties')
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        cher = str(input() )     #Challenger
        npc = random.choice(['r', 'p', 's'])
        if cher != 'r' and cher != 'p'and cher != 's' and cher != 'q':
            print('Error!!!\n')
            continue
        elif cher == 'q':
            print('Bye! Bye!')
            break
        print(move_is(cher) + ' versus...\n' + move_is(npc))
        if cher == npc:
            print('It is a tie!\n')
            t = t + 1
            continue
        elif cher == 'p' and npc == 'r':
            print('You win!\n')
            w = w + 1
            continue
        elif cher == 'p' and npc == 's':
            print('You losses!\n')
            l = l + 1
            continue
        elif cher == 's' and npc == 'p':
            print('You win!\n')
            w = w + 1
            continue
        elif cher == 's' and npc == 'r':
            print('You losses!\n')
            l = l + 1
            continue
        elif cher == 'r' and npc == 's':
            print('You win!\n')
            w = w + 1
            continue
        elif cher == 'r' and npc == 'p':
            print('You losses!\n')
            l = l + 1
            continue


def move_is(move):
    if move == 'r':
        return('ROCK')
    elif move == 'p':
        return('PAPER')
    elif move == 's':
        return('SCISSORS')
                


if __name__ == '__main__':
    hw_week8()
