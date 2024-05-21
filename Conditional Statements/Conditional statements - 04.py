vacation_price = float(input())
puzzels = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

sum_puzzels = puzzels * 2.6
sum_dolls = dolls * 3
sum_bears = bears * 4.1
sum_minions = minions * 8.2
sum_trucks = trucks * 2

sum = sum_puzzels + sum_dolls + sum_bears + sum_minions + sum_trucks

if puzzels + dolls + bears + minions + trucks >= 50:
    sum = sum - (sum * 0.25)

vacation_budget = sum - (sum * 0.1)

if vacation_budget >= vacation_price:
    money_left = vacation_budget - vacation_price
    print(f"Yes! {money_left:.2f} lv left.")
elif vacation_budget < vacation_price:
    money_needed = vacation_price - vacation_budget
    print(f"Not enough money! {money_needed:.2f} lv needed.")
