# Pangpoon Project
# 010123102 Programming Fundamentals
#
# Coding by Jirawat Yuktawathin
#
# Start 8 November 2016
# End 22 November 2016

import time

import menu
import main
import food
import welcome

# Set variable report from report.txt
report = 0
file = open('report.txt','r')
for lineR in file:
  report = int(lineR)
file.close()

# Print line
def println(count):
  for i in range(15 - count):
    print('#' + ' ' * 78 + '#')


class Call_payment:
  price = 0
  pay = 0
  countP = 0
  stringP = []

  def __init__(self):

    ''' Get input from user

If 'e' or 'E', go back to order (order.py)

Else if 'q' or 'Q', go back to welcome (welcome.py)

Else if more than price of all order, go to change (change.py)

Else, get input from user again

The write report in text file and go back to welcome (welcome.py) '''

    promotion = []
    shoplist = menu.shoplist

    # Open promotion file and read it (promotion.txt)
    file = open('promotion.txt', 'r')

    # Split each line from promotion file with ','
    # Then, append them to promotion list
    # Delete the last from each split
    for line in file:
      for item in line.split(','):
        promotion.append(item)
      del promotion[-1]

    # Calculate cash to pay
    for i in range(1, len(shoplist), 2):
      Call_payment.price += int(shoplist[i])

    # Calculate cash pay less from promotion
    for j in range(0, len(promotion), 3):
      Call_payment.price = Call_payment.price + (int(promotion[j + 2]) * \
(shoplist.count(promotion[j]) // int(promotion[j + 1])))

    file.close()

    for k in range(0, len(promotion), 3):
      if shoplist.count(promotion[k]) >= 3:
        Call_payment.stringP.append('# Promotion : Every '  + ' ' * (2 - len(promotion[k + 1])) + \
promotion[k + 1] + ' pieces of ' +  promotion[k] + ' ' * (25 - len(promotion[k])) + 'pay less ' + \
str(abs(int(promotion[k + 2]))) + ' Baht')
        Call_payment.countP += 1

    print('''############################## PangPoon - Payment ##############################
#                                                                              #''')
    # Show promotion to user if user buy an item in promotion
    for l in Call_payment.stringP:
      print(l + ' ' * (79 - len(l)) + '#')

    if len(Call_payment.stringP) > 0:
      print('#' + ' ' * 78 + '#')
      print('#' + ' ' * 78 + '#')
      Call_payment.countP += 2

    # Show to user how much to pay
    Call_payment.stringP.append('# Total ' + str(int(len(shoplist) / 2)) + ' orders ' + \
str(Call_payment.price) + ' Baht')
    print(Call_payment.stringP[-1] + ' ' * (79 - len(Call_payment.stringP[-1])) + '#')

    print('#' + ' ' * 78 + '#')
    print('#' + ' ' * 78 + '#')

    # Show price of order to user
    Call_payment.stringP.append('#' + ' ' * 25 + 'Price   :' + ' ' * (9 - len(str(float(Call_payment.price)))) + \
str(float(Call_payment.price)) + ' Baht')
    print(Call_payment.stringP[-1] + ' ' * (79 - len(Call_payment.stringP[-1])) + '#')

    print('#' + ' ' * 78 + '#')

    # Show how many user pay
    if Call_payment.pay > 0:
      Call_payment.stringP.append('#' + ' ' * 25 + 'Pay     :' + ' ' * (9 - len(str(Call_payment.pay))) + \
str(Call_payment.pay) + ' Baht')
      print(Call_payment.stringP[-1] + ' ' * (79 - len(Call_payment.stringP[-1])) + '#')

      Call_payment.stringP.append('#' + ' ' * 25 + 'Change  :' + \
' ' * (9 - len(str(Call_payment.pay - Call_payment.price))) + str(Call_payment.pay - Call_payment.price) + ' Baht')
      print(Call_payment.stringP[-1] + ' ' * (79 - len(Call_payment.stringP[-1])) + '#')

      Call_payment.countP += 2

    println(Call_payment.countP)

    if Call_payment.pay > 0:
      print('''############################# Please press any key #############################''')

      choice = input()
      global report

      today = time.strftime('%Y%m%d')
      now = time.strftime('%H%M%S')

      # Write a report in new file
      file = open(today + '_' + now + '_' + str(report) + '.txt', 'w')
      for m in range(0, len(shoplist), 2):
        file.write(shoplist[m] + ' ' * (30 - len(shoplist[m])) + ' ' * (2 - len(shoplist[m + 1])) + \
shoplist[m + 1] + ' Baht')
        file.write('\n')
      file.write('\nTotal ' + str(int(len(shoplist) / 2)) + ' orders ' + str(Call_payment.price) + ' Baht')
      file.close()

      report += 1

      file = open('report.txt', 'w')
      file.write(str(report))
      file.close()

      Call_payment.price = 0
      Call_payment.pay = 0
      Call_payment.countP = 0
      Call_payment.stringP = []

      menu.shoplist = []

      welcome.Call_welcome()
    else:
      print('''# Number of cash to pay ## E to edit order ## Q to cancel ######################''')

      while True:
        choice = input()

        try:

          if choice == 'q' or choice == 'Q':
            break
          elif choice == 'e' or choice == 'E':
            break
          elif 0 <= float(choice) < Call_payment.price:
            print('Not enough cash')
            continue
          elif float(choice) >= Call_payment.price:
            break

        except ValueError:
          pass

        print('Please try again')

      try:

        if choice == 'q' or choice == 'Q':
          Call_payment.price = 0
          Call_payment.pay = 0
          Call_payment.countP = 0
          Call_payment.stringP = []

          menu.shoplist = []

          main.Call_main()
        elif choice == 'e' or choice == 'E':
          Call_payment.price = 0
          Call_payment.pay = 0
          Call_payment.countP = 0
          Call_payment.stringP = []

          food.Call_food()
        elif float(choice) >= Call_payment.price:
          Call_payment.price = 0
          Call_payment.pay = float(choice)
          Call_payment.countP = 0
          Call_payment.stringP = []

          Call_payment()

      except ValueError:
        pass
