print('Let\'s play Rock Paper Scissors... also known as Janken.')
print('Rock beats Scissors, Scissors beats paper, and Paper beats Rock... simple.')
print('In order to play fair I will import an RNG... as for you...')
import random

TheChoice = input('which will you Choose? ')

YourChoice = TheChoice.lower()

Rock = 'rock'
Scissors = 'scissors'
Paper = 'paper'

RNG_Digit = random.randint(0, 2)

if RNG_Digit == 0:
    PC_Choice = Rock
if RNG_Digit == 1:
    PC_Choice = Scissors
else: PC_Choice = Paper

R_ascii = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
P_ascii = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

S_ascii = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(f'You chose {YourChoice}')
if YourChoice == Rock:
    print(R_ascii)
if YourChoice == Paper:
    print(P_ascii)
if YourChoice == Scissors:
    print(S_ascii)
if YourChoice != Rock and YourChoice != Paper and YourChoice != Scissors:
    print('....................../´¯/)\n....................,/¯../\n...................,/¯../\n.................../..../\n............./´¯/\'...\'/´¯¯`·¸\n........../\'/.../..../......./¨¯\\\n........(\'(...´...´.... ¯~/\'...\'\)\n.........\.................\'...../\n..........\...\..........._.·´\n............\..............(\n..............\.............\...\nYOUR SELECTION IS NOT VALID!')

print(f'PC chose {PC_Choice}')
if PC_Choice == Rock:
    print(R_ascii)
if PC_Choice == Paper:
    print(P_ascii)
if PC_Choice == Scissors:
    print(S_ascii)

if PC_Choice != YourChoice:
    if PC_Choice == Rock and YourChoice == Paper:
        print('Paper wraps up Rock, YOU WIN!')
    if PC_Choice == Paper and YourChoice == Scissors:
        print('Scissors cuts Paper, YOU WIN!')
    if PC_Choice == Scissors and YourChoice == Rock:
        print('Rock smashes Scissors, YOU WIN!')
    if PC_Choice == Paper and YourChoice == Rock:
        print('Paper wraps up Rock, YOU LOSE!')
    if PC_Choice == Scissors and YourChoice == Paper:
        print('Scissors cuts Paper, YOU LOSE!')
    if PC_Choice == Rock and YourChoice == Scissors:
        print('Rock smashes Scissors, YOU LOSE!')
else: print('It seems you both picked the same one, you\'ll have to play again.')