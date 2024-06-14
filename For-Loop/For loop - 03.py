n = int(input())

p1_broi = 0
p2_broi = 0
p3_broi = 0
p4_broi = 0
p5_broi = 0

for numbers in range(n):
    numbers = int(input())
    
    if numbers < 200:
        p1_broi += 1
    elif 200 <= numbers <= 399:
        p2_broi += 1
    elif 400 <= numbers <= 599:
        p3_broi += 1
    elif 600 <= numbers <= 799:
        p4_broi += 1
    else:
        p5_broi += 1

print(f"{(p1_broi / n) * 100:.2f}%")
print(f"{(p2_broi / n) * 100:.2f}%")
print(f"{(p3_broi / n) * 100:.2f}%")
print(f"{(p4_broi / n) * 100:.2f}%")
print(f"{(p5_broi / n) * 100:.2f}%")
