name_actor = input()
points_from_academy = float(input())
amount_judges = int(input())

for _ in range(amount_judges):
    name_judge = input()
    points_judge = float(input())
    points_from_academy += ((len(name_judge) * points_judge)/ 2)

    if points_from_academy > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points_from_academy:.1f}!")
        break

if points_from_academy <= 1250.5:
    print(f"Sorry, {name_actor} you need {1250.5 - points_from_academy:.1f} more!")
