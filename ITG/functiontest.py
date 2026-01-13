print("ggt(a,b) berechnen")
a = int(input("a="))
b = int(input("b="))
while b!=0:
    rest = a % b 
    a = b
    b = rest
print("ggt(a,b)=",a) 
