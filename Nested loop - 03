prime = 0
non_prime = 0
flag = False

while True:
    command = input()
    if command == "stop":
        break
    num = int(command)
    if num < 0:
        print("Number is negative.")
    elif num == 1:
        non_prime += num
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                non_prime += num
                break
        else:
            prime += num
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
