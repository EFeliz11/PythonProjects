import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letter = random.randint(3, 6)
nr_capita = random.randint(3, 6)
nr_number = random.randint(2, 4)
nr_symbol = random.randint(1, 3)
sum = nr_letter + nr_capita + nr_number + nr_symbol

PassMix = []
Password = ''
print(len(PassMix))

for Char in range(1, nr_letter + 1):
    PassMix += random.choice(letters)

print(f'{nr_letter} added for Letters')
print(f'Total is {len(PassMix)}')

for Char in range(1, nr_capita + 1):
    PassMix += random.choice(capitals)

print(f'{nr_capita} added for CAPS')
print(f'Total is {len(PassMix)}')

for Char in range(1, nr_number + 1):
    PassMix += random.choice(numbers)

print(f'{nr_number} added for 9umbers')
print(f'Total is {len(PassMix)}')

for Char in range(1, nr_symbol + 1):
    PassMix += random.choice(symbols)

print(f'{nr_symbol} added for $ymbols')
print(f'Total is {len(PassMix)}')

random.shuffle(PassMix)

print(f'Total Characters is {len(PassMix)}')

for Char in PassMix:
    random.choice(PassMix)
    Password += random.choice(PassMix)

print(f'Password is: {Password}')