age = int(input())
price_washer = float(input())
price_per_doll = int(input())

sum = 0
dolls = 0

for i in range(0, age + 1, 2):
    if i > 0:
        sum += 10 * (i / 2)

for i in range(1, age + 1, 2):
    dolls += 1

money_from_dolls = dolls * price_per_doll
all_sum = (sum - (age // 2)) + money_from_dolls

if all_sum >= price_washer:
    print(f"Yes! {all_sum - price_washer:.2f}")
elif price_washer > all_sum:
    print(f"No! {price_washer - all_sum:.2f}")
