#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
问题描述
　　小葱喜欢除法，所以他给了你N个数a1, a2, ⋯, aN，并且希望你执行M次操作，每次操作可能有以下两种：
　　给你三个数l, r, v，你需要将al, al+1, ⋯, ar之间所有v的倍数除以v。
　　给你两个数l, r，你需要回答al + al+1 + ⋯ + ar的值是多少。
输入格式
　　第一行两个整数N, M，代表数的个数和操作的次数。
　　接下来一行N个整数，代表N个数一开始的值。
　　接下来M行，每行代表依次操作。每行开始有一个整数opt。如果opt=1，那么接下来有三个数l, r, v，代表这次操作需要将第l个数到第r个数中v的倍数除以v；如果opt = 2，那么接下来有两个数l, r，代表你需要回答第l个数到第r个数的和。
输出格式
　　对于每一次的第二种操作，输出一行代表这次操作所询问的值。
样例输入
5 3
1 2 3 4 5
2 1 5
1 1 3 2
2 1 5
样例输出
15
14
评测用例规模与约定
　　对于30%的评测用例，1 ≤ N, M ≤ 1000；
　　对于另外20%的评测用例，第一种操作中一定有l = r；
　　对于另外20%的评测用例，第一种操作中一定有l = 1 , r = N；
　　对于100%的评测用例，1 ≤ N, M ≤ 105，0 ≤ a1, a2, ⋯, aN ≤ 106, 1 ≤ v ≤ 106, 1 ≤ l ≤ r ≤ N。

'''


# 以下提交时30分

a = list(map(int, input().split()))
n, m = a[0], a[1]
all = list(map(int, input().split()))


for i in range(m):
    stdin = list(map(int, input().split()))
    if stdin[0]-1:
        if stdin[1]-1 == stdin[2]:
            print(all[stdin[1]-1])
        else:
            temp = all[stdin[1]-1:stdin[2]]
            print(sum(temp))
    else:
        for j in range(stdin[1]-1, stdin[2]):
            if all[j]%stdin[3] == 0:
                all[j] = all[j]//stdin[3]
