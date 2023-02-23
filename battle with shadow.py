import random

min_health = 0
max_health = 20
player_health = max_health
bot_health = max_health

#spell 
spells = [['fireball', 10,0], ['matabolism',0, 8], ['silience',0, 0]]
name = 0
damage = 1
heal = 2

print('''=============НАСТРОЙКИ===================
        
        способности     Урон     ХИЛКА    ''')
i = 1
for row in spells:
    print(f'\n{[i]}', end=' - ')
    i+=1
    for elem in row:
        print('\t', elem, end='')
print(f'''
=============================================
================ДУЭЕЛЬ С ПРИВЕДЕНИЕМ=========
       Player          vs        BOT
    {player_health}                    {bot_health}
    
=============================================''')

new_round = '''
.....__.............................@......
..._##_............................._##_...
...##|_..............................###...
.._##._####.........#.#........_####__##_..
...###.####...._###-...|###_..._####_##@_..
..._@###____####._.......__####__._###_....
.....########._.............._########_....
.._######__......................_######_..
_####_.$####$................_#####-._####.
_##......._###_.............-###_.......##_
_##........._##@._......._.###........._##_
####........._####.......####..........####
...........................................
'''
win='''
##########################################
################_||||#||||_###############
###########|||||||||||||||||||||##########
##########$|||||||||||||||||||||$#########
######|||||||||||||||||||||||||||||||#####
######|||||||||__-$$$$$$$$$$|||||||||#####
##$||||||||$|||$$$$$$$$$$$$$|||$||||||||##
###|||||||||$|||$$$$$$$$$$$@||$|||||||||##
####|||||||||$$||$$$$$$$$$|||$|||||||||###
#$||||||||||||||$$$$$$$$$$$@|||||||||||||#
#||||||||||||||||||$$$$$|||||||||||||||||@
###|||||||||||||||||$$$$|||||||||||||||@##
##|||||||||||||||||$$$$$||||||||||||||||$#
#||||||||||||||||||$$$$$$||||||||||||||||@
####-||||||||||||$$$$$$$$$||||||||||||-###
####|||||||||||||$$$$$$$$$||||||||||||-###
####|||||||||||||$$$$$$$$$|||||||||||||###
########||||||||@@||@@@@@@@||||||||#######
########||||||||||||||||||||||||||$#######
#############||||||||||||||||$############
##############||###$|||###$||#############
'''

while True:
    #Player
  print('\nНАЧАТЬ ДУЕЛЬ?\n[Y] - Yes\n[N] - No')
  select = input('ВАШ ВЫБОР: ')
  if select =='N' or select =='n':
      break
  elif (not select =='Y') and (not select == 'y'):
      print('ОШЫБКА! ПОПРОБУЙТЕ ЕЩЁ.')
  else:
        #new game
      print('===========================')
      for round in range(1, 4):
          choice = True
          while choice:
              player_select = input('\nВЫБЕРИ АТАКУ: ')
              if player_select > '0' and player_select <= str(len(spells)):
                  player_select = int(player_select)
                  player_select = player_select - 1
                  bot_select = random.randint(0, len(spells)-1)
                  choice = False
              else:
                  print('Ошыбка! Попробуй снова.')
                        
          play_1 = spells[player_select][name]
          play_2 = spells[bot_select][name]
                
          if play_1 == 'silence' and play_2 == 'silence':
              print(f'''
          ---РАУНД № {round}----
          ------SILENCE------
          ''')
              continue
          elif play_1 == 'silence':
              player_select = bot_select
              player_health += spells[bot_select][damage]
          elif play_2 == 'silence':
              bot_select = player_select
              bot_health += spells[player_select][damage]
                    
          player_health += spells[player_select][heal]
          player_health -= spells[bot_select][damage]
          bot_health += spells[bot_select][heal]
          bot_health -= spells[player_select][damage]
                
          if player_health > max_health and bot_health > max_healh:
              player_health = max_health
              bot_health = max_health
          elif player_health > max_health:
              player_health = max_health
          elif bot_health > max_health:
              bot_health = max_health
          print(f'''
          ----РАУНД № {round}----{new_round}
          Player: {play_1}
          Play health: {player_health}
                
          Bot: {play_2}
          Bot health: {bot_health}''')
          if player_health < min_health or bot_health < min_health:
              break
                
      print('''=================================''')
      if player_health > bot_health:
          print('Поздравляем! ВЫ ВЫЙГРАЛИ!')
      elif player_health < bot_health:
          print('ВЫ ПРОИГРАЛИ ХАХА!')
      else:
          print('Draw!')
      print(win,'\n=======================================')