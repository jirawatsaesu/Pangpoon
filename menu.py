# Pangpoon Project
# 010123102 Programming Fundamentals
#
# Coding by Jirawat Yuktawathin
#
# Start 8 November 2016
# End 22 November 2016

menu = []

coffee = {}
beverage = {}
food = {}

counln = 0

shoplist = []

# Open menu file and read it (menu.txt)
file = open('menu.txt', 'r')

# Split menu.txt with line, then append to menu list
# Split each line from menu list with ','
for line in file:
  menu.append(line.split(','))

  # Sort item by type
  # Then, delete the first and the last from each split
  # Finally, append to each dictionary
  for item in menu:

    # Beverage
    if item[0] == 'B':
      del item[0]
      del item[-1]
      beverage[item[0]] = item[1]

    # Coffee
    elif item[0] == 'C':
      del item[0]
      del item[-1]
      coffee[item[0]] = item[1]

    # Food
    elif item[0] == 'F':
      del item[0]
      del item[-1]
      food[item[0]] = item[1]

file.close()

# Repeat format print order
def shoplist_print(sequen, name, price):
  order = ' ' * (2 - len(str(sequen))) + ' [' + str(sequen) + '] ' + name + \
' ' * (27 - len(name) - len(price)) + price + ' Baht #'
  return order

# Repeat format print menu
def format_print(sequen, item, kind):
  menu = '#' + ' ' * (2 - len(str(sequen))) + ' [' + str(sequen) + '] ' + item + \
' ' * (26 - len(item) - len(kind[item])) + str(kind[item]) + ' Baht #'
  return menu

# Repeat print line
def println(round18, count, space = ' ' * 39):
  for i in range(0, 18 * round18 - count):
    print('#                                      #{}#'.format(space))


# For beverage.py
class Beverage:
  countB = 0
  orderB = {}
  roundB = 1
  sequenB = 1
  stringB = []

  # Set beverage ID
  def __init__(self):
    for itemB in beverage:
      Beverage.countB += 1
      Beverage.orderB[Beverage.countB] = itemB

    while Beverage.sequenB <= 18 * Beverage.roundB and Beverage.sequenB <= len(beverage):
      Beverage.stringB.append(format_print(Beverage.sequenB, Beverage.orderB[Beverage.sequenB], \
beverage))
      Beverage.sequenB += 1


# For coffee.py
class Coffee:
  countC = 0
  orderC = {}
  roundC = 1
  sequenC = 1
  stringC = []

  # Set coffee ID
  def __init__(self):
    for itemC in coffee:
      Coffee.countC += 1
      Coffee.orderC[Coffee.countC] = itemC

    while Coffee.sequenC <= 18 * Coffee.roundC and Coffee.sequenC <= len(coffee):
      Coffee.stringC.append(format_print(Coffee.sequenC, Coffee.orderC[Coffee.sequenC], coffee))
      Coffee.sequenC += 1


# For food.py
class Food:
  countF = 0
  orderF = {}
  roundF = 1
  sequenF = 1
  stringF = []

  # Set food ID
  def __init__(self):
    for itemF in food:
      Food.countF += 1
      Food.orderF[Food.countF] = itemF

    while Food.sequenF <= 18 * Food.roundF and Food.sequenF <= len(food):
      Food.stringF.append(format_print(Food.sequenF, Food.orderF[Food.sequenF], food))
      Food.sequenF += 1

# For order.py
class Order:
  countO = 0
  roundO = 1
  sequenO = 1
  stringO = []

  def __init__(self):
    for itemO in shoplist:
      Order.countO += 0.5

    if len(shoplist) > 0:
      while Order.sequenO <= 18 * Order.roundO and Order.sequenO <= len(shoplist) / 2:
        Order.stringO.append(shoplist_print(Order.sequenO, shoplist[(Order.sequenO - 1) * 2], \
shoplist[(Order.sequenO - 1) * 2 + 1]))
        Order.sequenO += 1
