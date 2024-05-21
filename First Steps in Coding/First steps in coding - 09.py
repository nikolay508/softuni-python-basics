dyl = int(input())
shir = int(input())
vis = int(input())
procent = float(input())
sum_procent = procent / 100
all_sum = dyl * shir * vis
sum_into_litres = all_sum * 0.001
print(sum_into_litres * (1 - sum_procent))
