from datetime import datetime
from datetime import date

today = date.today()
today = today.strftime("%d/%m/%Y")

user_choice = input('\n\n\n\n\n\n\n\n\n\n          Welcome to the Spooktober Check 3000!\n   Would you like to check if it\'s Halloween?!? (y/n): ')
while user_choice not in 'yn':
    user_choice = input('   Sorry, please choose y or n. (y/n): ')
if user_choice == 'y':
    input('\n\n     Okay, let me check the old Spook-O-Meter here...\n\n\n\n\n')
    if today == '31/10/2022':
        print("            Man this thing's going crazy!!!\n\n              Happy Halloween!!! 🎃👻🕸️")
    else:
        print("Hmm, not quite Halloween yet!")
elif user_choice == 'n':
    print('             Okay then, stay safe out there!')


