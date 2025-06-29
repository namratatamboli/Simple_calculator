#  python mini_projects/simple_calculator/main.py

try :
    a= float(input("\nEnter first number  : "))
    b= float(input("Enter second number : "))

    print("\nWhich operation you want to perform ?\n+ : addition\n- : subtraction\n* : multiplication\n/ : division\n")

    o= input("Enter Operation to be performed : ")

    match o :
        case "+" :
            print(f"\n{a} + {b} = {a+b}\n")
        case "-" :
            print(f"\n{a} - {b} = {a-b}\n")
        case "*" :
            print(f"\n{a} * {b} = {a*b}\n")
        case "/" :
            print(f"\n{a} / {b} = {a/b}\n")
        case _:
            print("\nInvalid operation. Please choose +, -, *, or /.\n")


except ValueError:
    print("Please enter valid numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("Unexpected error:", e)



