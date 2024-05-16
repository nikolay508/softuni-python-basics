number_fails_allowed = int(input())

average = 0
amount = 0
fail = 0
last_problem = str

name = input()
while name != "Enough":
    grade = float(input())
    average += grade
    last_problem = name
    amount += 1
    if grade <= 4.00:
        fail += 1
    if fail >= number_fails_allowed:
        print(f"You need a break, {fail} poor grades.")
        break
    name = input()

if name == "Enough":
    print(f"Average score: {average / amount:.2f}")
    print(f"Number of problems: {amount}")
    print(f"Last problem: {last_problem}")
