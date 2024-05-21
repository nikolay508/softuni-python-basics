flowers_type = input()
broi = int(input())
budget = int(input())

price = 0

if flowers_type == "Roses":
    price = 5 * broi
elif flowers_type == "Dahlias":
    price = 3.80 * broi
elif flowers_type == "Tulips":
    price = 2.80 * broi
elif flowers_type == "Narcissus":
    price = 3 * broi
elif flowers_type == "Gladiolus":
    price = 2.50 * broi

if flowers_type == "Roses":
    if broi > 80:
        price = price - (0.1 * price)
elif flowers_type == "Dahlias":
    if broi > 90:
        price = price - (0.15 * price)
elif flowers_type == "Tulips":
    if broi > 80:
        price = price - (0.15 * price)
elif flowers_type == "Narcissus":
    if broi < 120:
        price = price + (0.15 * price) #dobavqme discount (oskypqvane)
elif flowers_type == "Gladiolus":
    if broi < 80:
        price = price + (0.20 * price) #dobavqme discount (oskypqvane)

if budget >= price:
    print(f"Hey, you have a great garden with {broi} {flowers_type} and {budget - price:.2f} leva left.")
elif budget < price:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
