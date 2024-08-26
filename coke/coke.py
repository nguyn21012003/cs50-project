amount_due = 50
print("Amount Due:", amount_due)
while amount_due > 0:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in [5, 10, 25]:
        amount_due -= insert_coin
        if amount_due <= 0:
            change_owed = abs(amount_due)
            print("Change Owed:", change_owed)
        else:
            print("Amount Due:", amount_due)
    else:
        print("Amount Due:", amount_due)
