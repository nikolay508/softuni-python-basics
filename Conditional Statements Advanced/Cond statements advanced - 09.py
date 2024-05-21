days = int(input()) #0-365
type = input() #room for one person / apartment / president apartment
grade = input() #positive / negative

noshtuvki = days - 1 
price = 0
if type == "room for one person":
    price = 18 * noshtuvki
elif type == "apartment":
    price = 25 * noshtuvki
elif type == "president apartment":
    price = 35 * noshtuvki

if days < 10:
    if type == "apartment":
        price = price - (0.3 * price)
    elif type == "president apartment":
        price = price - (0.1 * price)
elif 10 <= days <= 15:
    if type == "apartment":
        price = price - (0.35 * price)
    elif type == "president apartment":
        price = price - (0.15 * price)
elif days > 15:
    if type == "apartment":
        price = price - (0.50 * price)
    elif type == "president apartment":
        price = price - (0.20 * price)

if grade == "positive":
    price = price + (0.25 * price)
    print(f"{price:.2f}")
elif grade == "negative":
    price = price - (0.1 * price)
    print(f"{price:.2f}")
