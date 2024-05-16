steps = input()
goal = 10000
all_sum = 0

while steps != "Going home":
    steps_sum = int(steps)
    all_sum += steps_sum
    if all_sum >= goal:
        print("Goal reached! Good job!")
        print(f"{all_sum - goal} steps over the goal!")
        break
    steps = input()

if steps == "Going home":
    steps_to_home = int(input())
    if goal > steps_to_home + all_sum:
        print(f"{goal - (all_sum + steps_to_home)} more steps to reach goal.")
    elif goal < steps_to_home + all_sum:
        print("Goal reached! Good job!")
        print(f"{(all_sum + steps_to_home) - goal} steps over the goal!")
