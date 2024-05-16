N = int(input())

for number in range(1111, 9999 +1):
    number_str = str(number)
    special = True
    for digit in number_str:
        if int(digit) == 0 or N % int(digit) != 0:
            special = False
            break
    if special:
        print(number, end=" ")
