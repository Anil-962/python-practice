
def cal_total(exp):
    total = 0
    for item in exp:
        total = total+item
    return total

Ani_exp = [21000,2334,4556]
Mani_exp = [2000,3400,34556]

Ani_total = cal_total(Ani_exp)
Mani_exp = cal_total(Mani_exp)
print("Ani's Total Exp",Ani_total)
print("Mani's Total Exp",Mani_exp)
