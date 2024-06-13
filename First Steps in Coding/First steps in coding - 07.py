chicken_meal = float(input())
fish_meal = float(input())
vegan_meal = float(input())

sum_chicken = chicken_meal * 10.35
sum_fish = fish_meal * 12.4
sum_vegan = vegan_meal * 8.15
all_meals = sum_chicken + sum_fish+ sum_vegan
desert = 0.2 * all_meals

print(all_meals + desert + 2.5)
