# 题目：企业发放的奖金根据利润提成。
# 利润(I) --- 大于部分提成
# I<=1OW --- 10%
# I<=20W --- 7.5%
# I<=40W --- 5%
# I<=60W --- 3%
# I<=100W --- 1.5%
# I>100W --- 1%
# 从键盘输入当月利润I，求应发放奖金总数？
i = int(input('当月利润:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += (i - arr[idx])*rat[idx]
        i = arr[idx]
print('应发奖金：', r)
