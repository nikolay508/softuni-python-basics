width_apartment = int(input())
length_apartment = int(input())
height_apartment = int(input())

V_apartment = width_apartment * length_apartment * height_apartment
V_box = 1

command = input()
while command != "Done":
    num = int(command)
    V_apartment -= num
    if V_apartment <= 0:
        print(f"No more free space! You need {abs(V_apartment)} Cubic meters more.")
        break
    command = input()

if command == "Done":
    print(f"{V_apartment} Cubic meters left.")
