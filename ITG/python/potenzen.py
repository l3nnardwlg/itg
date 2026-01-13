
def pot(x, y):
    return x ** y


print("was machen?.")
print("1. Potenzieren")


while True:
    # take input from the user
    choice = input("auswahl(1): ")

    # check if choice is one of the four options
    if choice in ('1'):
        try:
            num1 = float(input("Basis "))
            num2 = float(input("Exponent "))
        except ValueError:
            print("err.")
            continue

        if choice == '1':
            print(num1, "^", num2, "=", pot(num1, num2))
        

        next_calculation = input("nochmal?? (ja/nein): ")
        if next_calculation == "no":
          break
    else:
        print("error")