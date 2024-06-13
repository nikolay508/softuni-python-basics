pens = int(input())
markers = int(input())
preparat = int(input())
discount = int(input())

sum_pens = pens * 5.8
sum_mar = markers * 7.2
sum_pre = preparat * 1.2

all = sum_pens + sum_mar + sum_pre
sum_dis = (discount / 100) * all

print(all - sum_dis)
