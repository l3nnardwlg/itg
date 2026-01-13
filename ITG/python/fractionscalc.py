import sys  

def ggt(a, b):

    while b != 0:
        a, b = b, a % b
    return a


print("Bruchrechnung")

# 
try:
    z1 = int(input("Zähler 1 (z1) = "))
    n1 = int(input("Nenner 1 (n1) = "))
    z2 = int(input("Zähler 2 (z2) = "))
    n2 = int(input("Nenner 2 (n2) = "))
    
    if n1 == 0 or n2 == 0:
        print("Fehler: Ein Nenner darf nicht 0 sein!")
        sys.exit(1)
    
    op = input("Operation (+, -, *, /): ").strip()
except ValueError:
    print("Fehler: Bitte ganze Zahlen eingeben!")
    sys.exit(1)

# 
ze = 0
ne = 1

if op == '+':
    ze = z1 * n2 + z2 * n1
    ne = n1 * n2
elif op == '-':
    ze = z1 * n2 - z2 * n1
    ne = n1 * n2
elif op == '*':
    ze = z1 * z2
    ne = n1 * n2
elif op == '/':
    if z2 == 0:
        print("Fehler: Division durch Null (Zähler 2 = 0)!")
        sys.exit(1)
    ze = z1 * n2
    ne = n1 * z2
else:
    print("Fehler: Ungültige Operation! Nur +, -, *, / erlaubt.")
    sys.exit(1)

# 
if ne < 0:
    ze = -ze
    ne = -ne

# 
g = ggt(abs(ze), ne)
ze //= g
ne //= g

# 
if ne == 1:
    print(f"Ergebnis: {ze}")
elif ze == 0:
    print("Ergebnis: 0")
else:
    print(f"Ergebnis: {ze}/{ne}")