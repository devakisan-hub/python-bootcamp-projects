def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
operations = {"+": add, "-": subtract, "*" : multiply, "/": divide}
def calculator():
    logo = r"""
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    print(logo)
    should_continue = True
    f_num = float(input("Enter first number:"))
    while should_continue:
        print("+\n-\n*\n/\n")
        choice = input("Enter your choice:")
        l_num = float(input("Enter second number:"))
        if choice in operations:
            result = operations[choice](f_num, l_num)
            print(f"{f_num} {choice} {l_num} = {result}")
        else:
            print("Enter valid choice.")
        will_continue = input("Enter 'yes' if u want to continue or enter 'no'")
        if will_continue == "yes":
            y_or_n = input(f"Type 'y' to continue calculating with {result} or enter 'n' to continue with new values.")
            if y_or_n == "y":
                f_num = result
            else:
                should_continue = False
                print("\n"*20)
                calculator()
        else:
            should_continue = False
calculator()



