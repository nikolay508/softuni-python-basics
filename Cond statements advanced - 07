month = input()
days = int(input())

studio_price = 0
apartment_price = 0
discount_apartment = 0
discount_studio = 0

if month == "May" or month == "October":
    studio_price = 50 * days
    apartment_price = 65 * days
elif month == "June" or month == "September":
    studio_price = 75.20 * days
    apartment_price = 68.70 * days
elif month == "July" or month == "August":
    studio_price = 76 * days
    apartment_price = 77 * days

if month == "May" or month == "October":
    if days > 14:
        discount_studio = discount_studio + (0.3 * studio_price)
    elif days > 7:
        discount_studio = discount_studio + (0.05 * studio_price)
elif month == "June" or month == "September":
    if days > 14:
        discount_studio = discount_studio + (0.2 * studio_price)

if days > 14:
    discount_apartment = discount_apartment + (0.1 * apartment_price)

print(f"Apartment: {apartment_price - discount_apartment:.2f} lv.")
print(f"Studio: {studio_price - discount_studio:.2f} lv.")
