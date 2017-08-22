# Pangpoon Project
# 010123102 Programming Fundamentals
#
# Coding by Jirawat Yuktawathin
#
# Start 8 November 2016
# End 22 November 2016

import menu
import main
import beverage
import food
import payment

class Call_coffee:
  def __init__(self):

    # Call information of coffee and order
    menu.Order()
    menu.Coffee()

    countC = menu.Coffee.countC
    orderC = menu.Coffee.orderC
    roundC = menu.Coffee.roundC
    sequenC = menu.Coffee.sequenC
    stringC = menu.Coffee.stringC

    countO = menu.Order.countO
    roundO = menu.Order.roundO
    sequenO = menu.Order.sequenO
    stringO = menu.Order.stringO

    shoplist = menu.shoplist

    print('''############################## PangPoon - Coffee ###############################
#                                                                              #''')

    # Print all coffee and order
    if len(stringC) >= len(stringO):
      for i in range(len(stringC)):
        try:

          print(stringC[i] + stringO[i])

        except IndexError:
          print(stringC[i] + ' ' * 39 + '#')

      menu.println(roundC, countC)
    else:
      for j in range(len(stringO)):
        try:

          print(stringC[j] + stringO[j])

        except IndexError:
          print('#' + ' ' * 38 + '#' + stringO[j])
          menu.countln += 1

      menu.println(roundC, countC + menu.countln)

    print('''#                                                                              #
# Number to choose order ## D to delete order ## B to beverage ## F to food   ##
# Enter to more menu     ## O to more order   ## P to payment  ## Q to cancel ##''')

    ''' Get input from user

If 'Enter', show more coffee list

Else if 'q' or 'Q', cancel order and go back to main menu (main.py)

Else if 'd' or 'D', delete order

Else if 'b' or 'B', go to beverage (beverage.py)

Else if 'f' or 'F', go to food (food.py)

Else if 'p' or 'P', go to payment (payment.py)

Else if 'o' or 'O', show more order list

Else if between 0 to last number of coffee

Else, get input from user again '''

    while True:
      choice = list(input())
      strChoice = ''

      for k in range(len(choice)):
        strChoice += choice[k]

      choice = []
      for l in strChoice.split():
        choice.append(l)

      try:

        if choice == [] and sequenC - 1 == countC:
          break
        elif choice == [] and sequenC - 1 == 18 * roundC:
          break
        elif choice[0] == 'q' or choice[0] == 'Q':
          break
        elif choice[0] == 'd' or choice[0] == 'D':
          choice.append(countO)
          if len(shoplist) > 0 and 0 < int(choice[1]) <= countO:
            break
          elif len(shoplist) == 0:
            print('Your order list is empty')
            continue
        elif choice[0] == 'b' or choice[0] == 'B':
          break
        elif choice[0] == 'f' or choice[0] == 'F':
          break
        elif choice[0] == 'p' or choice[0] == 'P':
          if len(shoplist) > 0:
            break
          else:
            print('Your order list is empty')
            continue
        elif choice[0] == 'o' or choice[0] == 'O':
          break
        elif 0 < int(choice[0]) <= countC:
          break

      except ValueError:
        pass
      except IndexError:
        pass

      print('Please try again')

    try:

      if choice == [] and sequenC - 1 == countC:
        menu.Coffee.countC = 0
        menu.Coffee.roundC = 1
        menu.Coffee.sequenC = 1
        menu.Coffee.stringC = []
        menu.countln = 0

        if len(shoplist) == 0:
          pass
        elif len(stringO) == 0 and len(shoplist) > 0:
          menu.Order.roundO -= 1
          menu.Order.sequenO += 1
          menu.Order.stringO = []

        menu.Order.countO = 0

        Call_coffee()
      elif choice == [] and sequenC - 1 == 18 * roundC:
        menu.Coffee.countC = 0
        menu.Coffee.roundC += 1
        menu.Coffee.stringC = []
        menu.countln = 0

        if len(shoplist) == 0:
          pass
        elif len(stringO) == 0 and len(shoplist) > 0:

          menu.Order.roundO -= 1
          menu.Order.sequenO += 1
          menu.Order.stringO = []

        menu.Order.countO = 0

        Call_coffee()
      elif choice[0] == 'q' or choice[0] == 'Q':
        menu.Coffee.countC = 0
        menu.Coffee.roundC = 1
        menu.Coffee.sequenC = 1
        menu.Coffee.stringC = []
        menu.countln = 0

        menu.Order.countO = 0
        menu.Order.roundO = 1
        menu.Order.sequenO = 1
        menu.Order.stringO = []

        menu.shoplist = []

        main.Call_main()
      elif choice[0] == 'd' or choice[0] == 'D':

        del menu.shoplist[(int(choice[1]) - 1)  * 2]
        del menu.shoplist[(int(choice[1]) - 1)  * 2]

        if len(menu.shoplist) > 36:
          menu.Order.roundO += len(menu.shoplist) // 36
          menu.Order.sequenO -= len(stringO)
        else:
          menu.Order.roundO = 1
          menu.Order.sequenO = 1

        menu.Order.countO = 0
        menu.Order.stringO = []

        menu.Coffee.countC = 0
        menu.countln = 0

        Call_coffee()
      elif choice[0] == 'b' or choice[0] == 'B':
        menu.Coffee.countC = 0
        menu.Coffee.roundC = 1
        menu.Coffee.sequenC = 1
        menu.Coffee.stringC = []

        menu.Order.countO = 0

        beverage.Call_beverage()
      elif choice[0] == 'f' or choice[0] == 'F':
        menu.Coffee.countC = 0
        menu.Coffee.roundC = 1
        menu.Coffee.sequenC = 1
        menu.Coffee.stringC = []

        menu.Order.countO = 0

        food.Call_food()
      elif choice[0] == 'p' or choice[0] == 'P':
        menu.Coffee.countC = 0
        menu.Coffee.roundC = 1
        menu.Coffee.sequenC = 1
        menu.Coffee.stringC = []
        menu.countln = 0

        menu.Order.countO = 0
        menu.Order.roundO = 1
        menu.Order.sequenO = 1
        menu.Order.stringO = []

        payment.Call_payment()
      elif choice[0] == 'o' or choice[0] == 'O':
        if sequenO - 1 == countO:
          menu.Order.countO = 0
          menu.Order.roundO = 1
          menu.Order.sequenO = 1
          menu.Order.stringO = []
        elif sequenO - 1 == 18 * roundO:
          menu.Order.countO = 0
          menu.Order.roundO += 1
          menu.Order.stringO = []
        else:
          menu.Order.countO = 0
          menu.Order.stringO = []
          if len(shoplist) / 2 == sequenO - 1:
            menu.Order.roundO = 1

        menu.Coffee.countC = 0
        menu.countln = 0

        Call_coffee()
      elif 0 < int(choice[0]) <= countC:
        menu.Coffee.countC = 0
        menu.countln = 0

        menu.shoplist.append(orderC[int(choice[0])])
        menu.shoplist.append(menu.coffee[orderC[int(choice[0])]])

        menu.Order.countO = 0

        if len(menu.shoplist) >= 36 * roundO + 2:
          menu.Order.roundO += 1
          menu.Order.stringO = []

        Call_coffee()

    except ValueError:
      pass
    except IndexError:
      pass
