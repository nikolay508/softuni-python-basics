sum = 0
final = 0
num = 0

graders = int(input())
name_presentation = input()
while name_presentation != "Finish":
    num += 1
    for _ in range(graders):
        grades = float(input())
        sum += grades / graders
    print(f"{name_presentation} - {sum:.2f}.")
    final += sum
    sum = 0
    name_presentation = input()

if name_presentation == "Finish":
    print(f"Student's final assessment is {final / num:.2f}.")
