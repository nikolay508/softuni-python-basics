budget = float(input())
statisti = int(input())
dress_per_statist = float(input())

dekor = 0.1 * budget

if statisti > 150:
    dress_per_statist = dress_per_statist - (0.1 * dress_per_statist)

dress_sum = dress_per_statist * statisti

if dekor + dress_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {(dekor + dress_sum) - budget:.2f} leva more.")
elif dekor + dress_sum <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - (dekor + dress_sum):.2f} leva left.")
