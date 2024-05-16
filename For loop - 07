number_groups_climbers = int(input())

all_sum = 0
sum_musala = 0
sum_monblan = 0
sum_kilim = 0
sum_k2 = 0
sum_everest = 0

for _ in range(number_groups_climbers):
    number = int(input())
    all_sum += number
    if 0 < number <= 5:
        sum_musala += number
    elif 6 <= number <= 12:
        sum_monblan += number
    elif 13 <= number <= 25:
        sum_kilim += number
    elif 26 <= number <= 40:
        sum_k2 += number
    elif number >= 41:
        sum_everest += number

print(f"{sum_musala / all_sum * 100:.2f}%")
print(f"{sum_monblan/ all_sum * 100:.2f}%")
print(f"{sum_kilim / all_sum * 100:.2f}%")
print(f"{sum_k2 / all_sum * 100:.2f}%")
print(f"{sum_everest / all_sum * 100:.2f}%")
