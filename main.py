# Pangpoon Project
# 010123102 Programming Fundamentals
#
# Coding by Jirawat Yuktawathin
#
# Start 8 November 2016
# End 22 November 2016

import welcome
import food
import beverage
import coffee

class Call_main:
  def __init__(self):

    ''' Get input from user

If 'b' or 'B', go to beverage (beverage.py)

Else if 'c' or 'C', go to coffee (coffee.py)

Else if 'f' or 'F', go to food (food.py)

Else if 'q' or 'Q', go back to welcome (welcome.py)

Else, get input from user again '''

    print('''############################# PangPoon - Main menu #############################
#                                                                              #
#                                                                              #
#        #######################                #######################        #
#       ##                     ##              ##                     ##       #
#       ##  Press B(beverage)  ##              ##       Press F       ##       #
#       ##   Press C(coffee)   ##              ##                     ##       #
#       ##                     ##              ##     ***             ##       #
#       ##      **             ##              ##    *****            ##       #
#       ##      **         _   ##              ##    *****            ##       #
#       ##     *  *       /    ##              ##     ***      **     ##       #
#       ##     *~~*      /     ##              ##     **      *_ *    ##       #
#       ##     *  *   *~~*     ##              ##     *       *  *    ##       #
#       ##     *  *   *  *     ##              ##     **      *_ *    ##       #
#       ##     ****   ****     ##              ##     **      *  *    ##       #
#       ##                     ##              ##              **     ##       #
#       ##                     ##              ##                     ##       #
#       ##   Coffee & Drinks   ##              ##     Food & Bread    ##       #
#       ##                     ##              ##                     ##       #
#        #######################                #######################        #
#                                                                              #
#                             Press Q to previous                              #
################################################################################''')

    while True:
      choice = input()

      if choice == 'b' or choice == 'B':
        break
      elif choice == 'c' or choice == 'C':
        break
      elif choice == 'f' or choice == 'F':
        break
      elif choice == 'q' or choice == 'Q':
        break
      else:
        print('Please try again')

    if choice == 'b' or choice == 'B':
      beverage.Call_beverage()
    elif choice == 'c' or choice == 'C':
      coffee.Call_coffee()
    elif choice == 'f' or choice == 'F':
      food.Call_food()
    elif choice == 'q' or choice =='Q':
      welcome.Call_welcome()
