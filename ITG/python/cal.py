#addieren funktion
def add(x, y):
    return x + y

# subtrahieren funktion
def subtract(x, y):
    return x - y

# multiplizieren funktion
def multiply(x, y):
    return x * y

# dividieren funktion
def divide(x, y):
    return x / y


print("rechenart auswählen.")
print("1.addiern")
print("2.subtrahieren")
print("3.multiplizieren")
print("4.dividieren")

while True:
    # auswahl
    choice = input("Art wählen(1/2/3/4): ")

    # auswahl prüfen
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("erste zahl: "))
            num2 = float(input("zweite zahl: "))
        except ValueError:
            print("keine zahl!.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # nächste rechnung?

        next_calculation = input("nochmal?? (ja/ne): ")
        if next_calculation == "no":
          break
    else:
        print("fehler in eingabe")