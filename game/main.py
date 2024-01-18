import random
options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
draws = 0
rounds = 1

while True:
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)
  
  user_option = input('Elige piedra, papel o tijera => ')
  user_option = user_option.lower()
  computer_option = random.choice(options)
  
  print('user option =>', user_option)
  print('computer option =>', computer_option)
  
  if user_option == computer_option:
      print('Empate')
      draws += 1
  
  elif user_option == 'piedra':
      if computer_option == 'papel':
          print('Perdiste')
          computer_wins += 1
      else:
          print('Ganaste')
          user_wins += 1
  
  elif user_option == 'papel':
      if computer_option == 'tijera':
          print('Perdiste')
          computer_wins += 1
      else:
          print('Ganaste')
          user_wins += 1
  
  elif user_option == 'tijera':
      if computer_option == 'piedra':
          print('Perdiste')
          computer_wins += 1
      else:
          print('Ganaste')
          user_wins += 1
  
  else:
      print('Opción inválida')

  rounds += 1
  print(user_wins)
  print(computer_wins)
  print(draws)

  if computer_wins == 3:
    print('Perdiste todo')
    break
  elif user_wins == 3:
    print('Ganaste todo')
    break
  elif draws == 3:
    print('Empate todo')
    break