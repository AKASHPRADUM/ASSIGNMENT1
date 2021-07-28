a = int(input("enter yor 1st no."))
b = int(input("enter yor 2st no."))
c = int(input("enter yor 3st no."))

if a < b and a < c: print(f"a = {a} is smallest")
elif b < a and b < c: print(f"b = {b} is smallest")
else: print(f"c= {c} is smallest")