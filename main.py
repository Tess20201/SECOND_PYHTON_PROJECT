# define pizza size and prices
small = 100.00
add_medium = 125.00
large = 150.00
family = 200.00

# side and prices
small_pepperoni = 20
medium_large = 40
add_family = 50
cheese =20

total_bill = 0

# define loop
while True:
    print()
    print("!!!!! WELCOME TO PIZZA PLAZA JOINT !!!!!")
    print()
    menu_choice = input ("Please what would you like\n"
    "\n"
    "  s for small\n"
    "  m for medium\n"
    "  l for large\n"
    "  f for family\n"
    "please kindly place your order here\n"
    ".: ").lower()
    
    try:
        if menu_choice =="s":
            total_bill += small
            pepperoni = input("Please would you like pepperoni? yes/no:").lower()
            if pepperoni =="yes":
                total_bill += small_pepperoni
            
                extra_cheese = input("please would you like to add extra cheese? yes/no:"
                                    "\n ").lower()
                if extra_cheese == "yes":
                    total_bill += cheese
                
                    
                    print(f"... Total bill is {total_bill}\n"
                        "   Thank you for buying form us ")
                    
        elif menu_choice =="m":
            total_bill += add_medium
            pepperoni = input("Please would you like pepperoni? yes/no:")
            if pepperoni =="yes":
                total_bill +=medium_large
                extra_cheese = input("please would you like to add extra cheese? yes/no:\n"
                                    "")
                if extra_cheese =="yes":
                    total_bill += cheese
                    print(f"... Total bill is {total_bill}\n"
                        "   Thank you for buying form us ")
                    
        elif menu_choice =="l":
            total_bill += large
            pepperoni = input("Please would you like pepperoni? yes/no:")
            if pepperoni =="yes":
                total_bill += medium_large
                extra_cheese = input("please would you like to add extra cheese? yes/no:\n"
                                    "")
                if extra_cheese =="yes":
                    total_bill += cheese
                    print(f"... Total bill is {total_bill}\n"
                        "   Thank you for buying form us ")
                    
        elif menu_choice =="f":
            total_bill += family
            pepperoni = input("Please would you like pepperoni? yes/no:")
            if pepperoni =="yes":
                total_bill += add_family
                extra_cheese = input("please would you like to add extra cheese? yes/no:\n"
                                    "")
                if extra_cheese =="yes":
                    total_bill += cheese
                    print(f"... Total bill is {total_bill}\n"
                        "   Thank you for buying form us ")
                    
        else:
            print("Misleading guidance, please try again")
                    
            
            
    except ValueError:
        print("Kindly enter your valid value")
        