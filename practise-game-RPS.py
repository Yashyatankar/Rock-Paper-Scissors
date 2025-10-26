import random

player = None
option = ('Rock', 'Paper', 'Scissor')

while player not in option:
    player = input("Please enter Rock, Paper or Scissor: ").title()

com_ans = random.choice(option)

if player == com_ans:
    print(com_ans)
    print("It's a tie")
elif (player == 'Rock' and com_ans == 'Scissor') or (player == 'Paper' and com_ans == 'Rock') or (player == 'Scissor' and com_ans == 'Paper'):
    print(com_ans)
    print('player won')
else:
    print(com_ans)
    print('player lose')
