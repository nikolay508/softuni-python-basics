budget = int(input())
season = input()
broi_ribari = int(input())

naem = 0

if season == "Spring":
    naem = 3000
elif season == "Summer" or season == "Autumn":
    naem = 4200
elif season == "Winter":
    naem = 2600

if 0 < broi_ribari <= 6:
    naem = naem - (0.1 * naem)
elif 7 <= broi_ribari <= 11:
    naem = naem - (0.15 * naem)
elif broi_ribari >= 12:
    naem = naem - (0.25 * naem)

if broi_ribari % 2 == 0:
    if season != "Autumn":
        naem = naem - (0.05 * naem)

if budget >= naem:
    print(f"Yes! You have {budget - naem:.2f} leva left.")
elif budget < naem:
    print(f"Not enough money! You need {naem - budget:.2f} leva.")
