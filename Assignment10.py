a = int(input("Enter the  limit for loop"))
b = int(input("Enter your no."))
c= []
for i in range (1,a+1):
    if i%b == 0 :
        c.append(i)
print(c)