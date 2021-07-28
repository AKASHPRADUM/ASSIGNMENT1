no_of_tickets=int(input("enter no. of tickets (including child) "))
ticket_price = float(input("Enter ticket price "))
child = int(input("Enter no. of child btw 0 to 5 "))
minor = int(input("Enter no. of minors btw 5 to =11 "))
senior_citizen = int(input("Enter no. of senior citizen age >= 65 "))
amount = 0
total = minor + child + senior_citizen
Adult = no_of_tickets - total

if senior_citizen :
    amount += (ticket_price*senior_citizen)*80/100
if child  :
    amount += 0
if minor :
    amount += (ticket_price*minor)*50/100
if Adult :
    amount += (ticket_price*Adult)
print(f"Total amount is {amount}")
