budget = float(input())
season = input()

place = str
type_vacation = str
price = 0

if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        type_vacation = "Camp"
        price = 0.3 * budget
    elif season == "winter":
        type_vacation = "Hotel"
        price = 0.7 * budget
elif budget <= 1000:
    place = "Balkans"
    if season == "summer":
        type_vacation = "Camp"
        price = 0.4 * budget
    elif season == "winter":
        type_vacation = "Hotel"
        price = 0.8 * budget
elif budget > 1000:
    place = "Europe"
    if season == "summer" or season == "winter":
        type_vacation = "Hotel"
        price = 0.9 * budget

print(f"Somewhere in {place}")
print(f"{type_vacation} - {price:.2f}")
