budget = float(input()) 
videocards = int(input())
procecors = int(input())
ram = int(input())

price_videocards = videocards * 250  
price_procecor = 0.35 * price_videocards
price_ram = 0.1 * price_videocards

sum_procecor = procecors * price_procecor
sum_ram = ram * price_ram

all_prices = price_videocards + sum_procecor + sum_ram

if videocards > procecors:
    all_prices = all_prices - (all_prices * 0.15)

if budget >= all_prices:
    print(f"You have {budget - all_prices:.2f} leva left!")
else:
    print(f"Not enough money! You need {all_prices - budget:.2f} leva more!")
