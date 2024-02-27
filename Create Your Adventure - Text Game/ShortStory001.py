print('Welcome to a Short Story')
name = input('Hello, what is your name? ')


print('You were summoned to another world, typical Isekai story with three other heroes.')
print('You are told that you will be tasked with defeating the Monster King.')
print('Unfortunately, the princess who summoned you thinks you\'re particularly weak.')
print('You get teleported away to a dungeon.')
print('')

choice01 = input('\nYou\'re faced with a choice of waiting for help, or getting an move on: w or m? ')

if choice01 == 'm' or choice01 == 'M':
  print('\n\nYou wander around until finding a room and you see a vial on a table')
  choice02 = input('drink from it? y or n? ')
  if choice02 == 'y' or choice02 == 'Y':
    print('\nYou\'ve acquired several unique skills, you continue onward to try and escape the dungeon.')
  else:
    print('\nYou proceed onward to escape the chamber. The door locks behind you.')
  print('\nYou reach the main chamber of the dungeon, you can see what looks like a portal in next room.')
  print('As you approach, the vampire queen gets in your way.')
  choice03 = input('\nFight the Vampire Queen or Run? f or r? ')
  if choice03.lower() == 'f' and choice02.lower() == 'n':
    print('\nThe Vampire Queen overpowered you, and enjoyed a nice snack with your blood... Game Over.')
  if choice03.lower() == 'r' and choice02.lower() == 'n':
    print('\nThe Vampire Queen catches you, and quickly sedates you, by having a snack with your blood... Game Over.')
  if choice03.lower() == 'r' and choice02.lower() == 'y':
    print('\nIt seems the vial\'s boost allowed you to evade her, but as you tire she eventually catches you.')
    print('\nToo interesting to kill, the vamp charms you, you live the rest of your life enslaved... Game Over.')
  if choice03.lower() == 'f' and choice02.lower() == 'y':
    print('\nAfter an intense battle, you manage to damage her with a powerful attack and achieve victory.')
    print('You make it to the teleporter and make your escape, you now have the ability to take your revenge of the princess.')
    print('\n...End of Chapter...\n')
    print(f'Congratulations, {name} on your escape.\nAs Uncle Ben said, With Great Power, comes sweet revenge... probably.')
    print('\n...Actually that might\'ve been Edmond Dantes.')
else:
  print('\n\nYou fulfilled the princess\'s wish and died quietly.\n... Game Over, ya bum... -__- ')