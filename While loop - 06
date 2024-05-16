cake_width = int(input())
cake_height = int(input())

S_cake = cake_height * cake_width

command = input()
while command != "STOP":
    num = int(command)
    S_cake -= num
    if S_cake <= 0:
        print(f"No more cake left! You need {abs(S_cake)} pieces more.")
        break
    command = input()

if command == "STOP":
    print(f"{S_cake} pieces are left.")
