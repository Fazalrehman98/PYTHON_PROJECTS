import random

def computer_guess(x):
    low= 1
    high= x
    feedback=""
    while feedback!= 'c' :
        if low != high:
            guess= random.randint(low, high)
        else:
            guess = low # could be high or low b\c low=high
        feedback=input(f'if {guess} to high (H), too low (L), or correct (C)??').lower()
        if feedback=='h':
            high= guess-1
        elif feedback=='l':
            low=guess+1 
    print('yay, the computer guessed your number,{guess} correctly!')

computer_guess(10)