
"""
Written by Uchegbu Somtochukwu David on 25th of May 2020
A basic Rock, Paper and Scissors game

"""

import random


def game():
    print('This is a simple game of Rock, paper, and scissors'
          'You will be playing against the computer'
          'Note that all your entries must be in lowercase'
          'Let us begin :)')

    while True:
        playerInput = input('Enter your preferred choice: ')
        computerList = ['rock', 'paper', 'scissors']
        computerInput = random.choice(computerList)

        def rock():
            if playerInput == 'rock' and computerInput == 'paper':
                print('computer chose ' + computerInput)
                print('you win')
            elif playerInput == 'rock' and computerInput == 'scissors':
                print('computer chose ' + computerInput)
                print('you win')
            elif playerInput == 'rock' and computerInput == 'rock':
                print('computer chose ' + computerInput)
                print('stale game')

        def paper():
            if playerInput == 'paper' and computerInput == 'rock':
                print('computer chose ' + computerInput)
                print('computer won')
            elif playerInput == 'paper' and computerInput == 'scissors':
                print('computer chose ' + computerInput)
                print('computer won')
            elif playerInput == 'paper' and computerInput == 'paper':
                print('computer chose ' + computerInput)
                print('stale game')

        def scissors():
            if playerInput == 'scissors' and computerInput == 'rock':
                print('computer chose ' + computerInput)
                print('computer won')
            elif playerInput == 'scissors' and computerInput == 'paper':
                print('computer chose ' + computerInput)
                print('you win')
            elif playerInput == 'scissors' and computerInput == 'scissors':
                print('computer chose ' + computerInput)
                print('stale game')

        rock()
        paper()
        scissors()

        retry = input('Want to try again? ')
        if retry == 'yes':
            True
        else:
            quit()


game()
