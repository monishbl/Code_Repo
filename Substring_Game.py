string = 'BANANA'
vowels = 'AEIOU'

Player1 = 0
Player2 = 0

for i in range(len(string)):
    if string[i] in vowels:
        Player1 += (len(string) - i)
    else:
        Player2 += (len(string) - i)
    
if Player1 > Player2:
    print(f'Player1: {Player1}')
elif Player1 < Player2:
    print(f'Player2: {Player2}')
else:
    print('Draw')