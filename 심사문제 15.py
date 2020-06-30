age = int(input())
balance = 9000

if age>=7 and age<=12:
    balance_1 = balance - 650
    print(balance_1)
elif age>=13 and age<=18:
    balance_2 = balance - 1050
    print(balance_2)
elif age>=19:
    balance_3 = balance - 1250
    print(balance_3)
    
