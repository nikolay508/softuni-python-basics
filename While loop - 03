vacation_money = float(input())
available_money = float(input())

days = 0
days_spend = 0

while available_money < vacation_money and days_spend < 5:
    activity = input()
    sum_activity = float(input())
    days += 1
    if activity == 'save':
        available_money += sum_activity
        days_spend = 0
    elif activity == 'spend':
        available_money -= sum_activity
        days_spend += 1
        if available_money < 0:
            available_money = 0

if days_spend == 5:
    print("You can't save the money.")
    print(days)

if available_money >= vacation_money:
    print(f"You saved the money for {days} days.")
