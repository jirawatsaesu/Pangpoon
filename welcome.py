# Pangpoon Project
# 010123102 Programming Fundamentals
#
# Coding by Jirawat Yuktawathin
#
# Start 8 November 2016
# End 22 November 2016

import main

class Call_welcome:
  def __init__(self):

    ''' Get input from user

If 'enter', go to main menu (main.py)

Else if 'q' or 'Q', quit program

Else if 'r' or 'R', reset all variable in program

Else, get input from user again '''

    print('''################################################################################
#                                                                              #
#                                                                              #
#      ########    ########    ##     ##    ########                           #
#      ##    ##    ##    ##    ###    ##    ##    ##                           #
#      ##    ##    ##    ##    ####   ##    ##                                 #
#      ########    ########    ## ##  ##    ##  ####                           #
#      ##          ##    ##    ##  ## ##    ##    ##                           #
#      ##          ##    ##    ##   ####    ##    ##                           #
#      ##          ##    ##    ##    ###    ########                           #
#                                                                              #
#                                                                              #
#                           ########    ########    ########    ##     ##      #
#                           ##    ##    ##    ##    ##    ##    ###    ##      #
#                           ##    ##    ##    ##    ##    ##    ####   ##      #
#                           ########    ##    ##    ##    ##    ## ##  ##      #
#                           ##          ##    ##    ##    ##    ##  ## ##      #
#                           ##          ##    ##    ##    ##    ##   ####      #
#                           ##          ########    ########    ##    ###      #
#                                                                              #
#                                                                              #
#                             Please press any key                             #
# Enter to start ## Q to exit ## R to reset program ############################''')

    while True:
      choice = input()

      if choice == '':
        break
      elif choice == 'q' or choice == 'Q':
        break
      elif choice == 'r' or choice == 'R':
        break
      else:
        print('Please try again')

    if choice == '':
      main.Call_main()
    elif choice == 'r' or choice == 'R':
      file = open('report.txt', 'w')
      file.write('1')
      file.close()

      Call_welcome()
