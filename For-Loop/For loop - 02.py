n = int(input())

sum = 0
largest_number = 0

for nums in range(n):
    numbers = int(input())
    sum += numbers
    
    if numbers > largest_number:
        largest_number = numbers

if largest_number == sum - largest_number:
    print("Yes")
    print(f"Sum = {largest_number}")
else:
    print("No")
    print(f"Diff = {abs(largest_number - (sum - largest_number))}")
