import random
from scipy.stats import f, t
from prettytable import PrettyTable
from numpy.linalg import solve

#Варіант 116
x1_min = 10
x1_max = 50
x2_min = -20
x2_max = 60
x3_min = -20
x3_max = 20

x_av_max = (x1_max + x2_max + x3_max) / 3
x_av_min = (x1_min + x2_min + x3_min) / 3
y_max = int(200 + x_av_max)
y_min = int(200 + x_av_min)

m = 4

X11 = [-1, -1, -1, -1, 1, 1, 1, 1]
X22 = [-1, -1, 1, 1, -1, -1, 1, 1]
X33 = [-1, 1, -1, 1, -1, 1, -1, 1]


def sum2(x1, x2):
    xn = []
    for i in range(len(x1)):
        xn.append(x1[i] * x2[i])
    return xn


def sum3(x1, x2, x3):
    xn = []
    for i in range(len(x1)):
        xn.append(x1[i] * x2[i] * x3[i])
    return xn


X12 = sum2(X11, X22)
X13 = sum2(X11, X33)
X23 = sum2(X22, X33)
X123 = sum3(X11, X22, X33)

X00 = [1, 1, 1, 1, 1, 1, 1, 1]

print("y=b0+b1*x1+b2*x2+b3*x3+b12*x1*x2+b13*x1*x3+b23*x2*x3+b123*x1*x2*x3+b11*x1^2+b22*x2^2+b33*x3^2\n")
print("Кодовані значення X")
table1 = PrettyTable()
table1.add_column("№", (1, 2, 3, 4, 5, 6, 7, 8))
table1.add_column("X1", X11)
table1.add_column("X2", X22)
table1.add_column("X3", X33)
table1.add_column("X12", X12)
table1.add_column("X13", X13)
table1.add_column("X23", X23)
table1.add_column("X123", X123)
print(table1, "\n")
for i in range(1, m + 1):
    globals()['Y%s' % i] = [random.randrange(y_min, y_max, 1) for k in range(8)]
X1 = [x1_min, x1_min, x1_min, x1_min, x1_max, x1_max, x1_max, x1_max]
X2 = [x2_min, x2_min, x2_max, x2_max, x2_min, x2_min, x2_max, x2_max]
X3 = [x3_min, x3_max, x3_min, x3_max, x3_min, x3_max, x3_min, x3_max]
X12 = sum2(X1, X2)
X13 = sum2(X1, X3)
X23 = sum2(X2, X3)
X123 = sum3(X1, X2, X3)
X0 = [1] * 8
s1, s2, s3, s4, s5, s6, s7, s8 = 0, 0, 0, 0, 0, 0, 0, 0
for i in range(1, m + 1):
    s1 += globals()['Y%s' % i][0]
    s2 += globals()['Y%s' % i][1]
    s3 += globals()['Y%s' % i][2]
    s4 += globals()['Y%s' % i][3]
    s5 += globals()['Y%s' % i][4]
    s6 += globals()['Y%s' % i][5]
    s7 += globals()['Y%s' % i][6]
    s8 += globals()['Y%s' % i][7]

#Середнє значення функції відгуку за рядками
y1_av1 = s1 / m
y2_av2 = s2 / m
y3_av3 = s3 / m
y4_av4 = s4 / m
y5_av5 = s5 / m
y6_av6 = s6 / m
y7_av7 = s7 / m
y8_av8 = s8 / m
y_av = [round(y1_av1, 3), round(y2_av2, 3), round(y3_av3, 3), round(y4_av4, 3), round(y5_av5, 3), round(y6_av6, 3),
        round(y7_av7, 3), round(y8_av8, 3)]
sd1, sd2, sd3, sd4, sd5, sd6, sd7, sd8 = 0, 0, 0, 0, 0, 0, 0, 0
for i in range(1, m + 1):
    sd1 += ((globals()['Y%s' % i][0]) - y1_av1) ** 2
    sd2 += ((globals()['Y%s' % i][1]) - y2_av2) ** 2
    sd3 += ((globals()['Y%s' % i][2]) - y3_av3) ** 2
    sd4 += ((globals()['Y%s' % i][3]) - y4_av4) ** 2
    sd5 += ((globals()['Y%s' % i][4]) - y5_av5) ** 2
    sd6 += ((globals()['Y%s' % i][5]) - y6_av6) ** 2
    sd7 += ((globals()['Y%s' % i][6]) - y7_av7) ** 2
    sd8 += ((globals()['Y%s' % i][7]) - y8_av8) ** 2

#Дисперсія за рядками
d1 = sd1 / m
d2 = sd2 / m
d3 = sd3 / m
d4 = sd4 / m
d5 = sd5 / m
d6 = sd6 / m
d7 = sd7 / m
d8 = sd8 / m
disper = [round(d1, 3), round(d2, 3), round(d3, 3), round(d4, 3), round(d5, 3), round(d6, 3), round(d7, 3),
          round(d8, 3)]

print("Матриця планування для m=4")
table2 = PrettyTable()
table2.add_column("№", (1, 2, 3, 4, 5, 6, 7, 8))
table2.add_column("X1", X1)
table2.add_column("X2", X2)
table2.add_column("X3", X3)
table2.add_column("X12", X12)
table2.add_column("X13", X13)
table2.add_column("X23", X23)
table2.add_column("X123", X123)
for i in range(1, m + 1):
    table2.add_column("Y" + str(i), globals()['Y%s' % i])
table2.add_column("Y", y_av)
table2.add_column("S^2", disper)
print(table2, "\n")

b = [i for i in solve(list(zip(X0, X1, X2, X3, X12, X13, X23, X123)), y_av)]
b0, b1, b2, b3, b4, b5, b6, b7 = round(b[0], 3), round(b[1], 3), round(b[2], 3), round(b[3], 3), round(b[4], 3), round(
    b[5], 3), round(b[6], 3), round(b[7], 3)
print("y=" + str(b0) + "+" + str(b1) + "*x1+" + str(b2) + "*x2+" + str(b3) + "*x3+" + str(b4) + "*x1*x2+" + str(
    b5) + "*x1*x3+" + str(b6) + "*x2*x3+" + str(b7) + "*x1*x2*x3", "\n")

dcouple = [d1, d2, d3, d4, d5, d6, d7, d8]

m = 3
print("Критерій Кохрена")
Gp = max(dcouple) / sum(dcouple)
q = 0.05
f1 = m - 1
f2 = N = 8
fisher = f.isf(*[q / f2, f1, (f2 - 1) * f1])
Gt = round(fisher / (fisher + (f2 - 1)), 4)
print("Gp = " + str(Gp) + ", Gt = " + str(Gt))
if Gp > Gt:
    print("Дисперсія  неоднорідна , збільшуємо m")
    m += 1
else:
    print("Gp < Gt -> Дисперсія однорідна\n")
    print("Критерій Стьюдента")
    sb = sum(dcouple) / N
    ssbs = sb / N * m
    sbs = ssbs ** 0.5

    beta0 = (y1_av1 * 1 + y2_av2 * 1 + y3_av3 * 1 + y4_av4 * 1 + y5_av5 * 1 + y6_av6 * 1 + y7_av7 * 1 + y8_av8 * 1) / 8
    beta1 = (y1_av1 * (-1) + y2_av2 * (-1) + y3_av3 * (-1) + y4_av4 * (
        -1) + y5_av5 * 1 + y6_av6 * 1 + y7_av7 * 1 + y8_av8 * 1) / 8
    beta2 = (y1_av1 * (-1) + y2_av2 * (-1) + y3_av3 * 1 + y4_av4 * 1 + y5_av5 * (-1) + y6_av6 * (
        -1) + y7_av7 * 1 + y8_av8 * 1) / 8
    beta3 = (y1_av1 * (-1) + y2_av2 * 1 + y3_av3 * (-1) + y4_av4 * 1 + y5_av5 * (-1) + y6_av6 * 1 + y7_av7 * (
        -1) + y8_av8 * 1) / 8
    beta4 = (y1_av1 * 1 + y2_av2 * 1 + y3_av3 * (-1) + y4_av4 * (-1) + y5_av5 * (-1) + y6_av6 * (
        -1) + y7_av7 * 1 + y8_av8 * 1) / 8
    beta5 = (y1_av1 * 1 + y2_av2 * (-1) + y3_av3 * 1 + y4_av4 * (-1) + y5_av5 * (-1) + y6_av6 * 1 + y7_av7 * (
        -1) + y8_av8 * 1) / 8
    beta6 = (y1_av1 * 1 + y2_av2 * (-1) + y3_av3 * (-1) + y4_av4 * 1 + y5_av5 * 1 + y6_av6 * (-1) + y7_av7 * (
        -1) + y8_av8 * 1) / 8
    beta7 = (y1_av1 * (-1) + y2_av2 * 1 + y3_av3 * 1 + y4_av4 * (-1) + y5_av5 * 1 + y6_av6 * (-1) + y7_av7 * (
        -1) + y8_av8 * 1) / 8

    t0 = abs(beta0) / sbs
    t1 = abs(beta1) / sbs
    t2 = abs(beta2) / sbs
    t3 = abs(beta3) / sbs
    t4 = abs(beta4) / sbs
    t5 = abs(beta5) / sbs
    t6 = abs(beta6) / sbs
    t7 = abs(beta7) / sbs

    f3 = f1 * f2
    ttabl = round(abs(t.ppf(q / 2, f3)), 4)

    d = 8
    if (t0 < ttabl):
        print("t0 < ttabl, b0 не значимий")
        b0 = 0
        d = d - 1
    if (t1 < ttabl):
        print("t1 < ttabl, b1 не значимий")
        b1 = 0
        d = d - 1
    if (t2 < ttabl):
        print("t2 < ttabl, b2 не значимий")
        b2 = 0
        d = d - 1
    if (t3 < ttabl):
        print("t3 < ttabl, b3 не значимий")
        b3 = 0
        d = d - 1
    if (t4 < ttabl):
        print("t4 < ttabl, b4 не значимий")
        b4 = 0
        d = d - 1
    if (t5 < ttabl):
        print("t5 < ttabl, b5 не значимий")
        b5 = 0
        d = d - 1
    if (t6 < ttabl):
        print("t6 < ttabl, b6 не значимий")
        b6 = 0
        d = d - 1
    if (t7 < ttabl):
        print("t7 < ttabl, b7 не значимий\n")
        b7 = 0
        d = d - 1

    yy1 = b0 + b1 * x1_min + b2 * x2_min + b3 * x3_min + b4 * x1_min * x2_min + b5 * x1_min * x3_min + b6 * x2_min * \
          x3_min + b7 * x1_min * x2_min * x3_min
    yy2 = b0 + b1 * x1_min + b2 * x2_min + b3 * x3_max + b4 * x1_min * x2_min + b5 * x1_min * x3_max + b6 * x2_min * \
          x3_max + b7 * x1_min * x2_min * x3_max
    yy3 = b0 + b1 * x1_min + b2 * x2_max + b3 * x3_min + b4 * x1_min * x2_max + b5 * x1_min * x3_min + b6 * x2_max * \
          x3_min + b7 * x1_min * x2_max * x3_min
    yy4 = b0 + b1 * x1_min + b2 * x2_max + b3 * x3_max + b4 * x1_min * x2_max + b5 * x1_min * x3_max + b6 * x2_max * \
          x3_max + b7 * x1_min * x2_max * x3_max
    yy5 = b0 + b1 * x1_max + b2 * x2_min + b3 * x3_min + b4 * x1_max * x2_min + b5 * x1_max * x3_min + b6 * x2_min * \
          x3_min + b7 * x1_max * x2_min * x3_min
    yy6 = b0 + b1 * x1_max + b2 * x2_min + b3 * x3_max + b4 * x1_max * x2_min + b5 * x1_max * x3_max + b6 * x2_min * \
          x3_max + b7 * x1_max * x2_min * x3_max
    yy7 = b0 + b1 * x1_max + b2 * x2_max + b3 * x3_min + b4 * x1_max * x2_max + b5 * x1_max * x3_min + b6 * x2_max * \
          x3_min + b7 * x1_max * x2_max * x3_min
    yy8 = b0 + b1 * x1_max + b2 * x2_max + b3 * x3_max + b4 * x1_max * x2_max + b5 * x1_max * x3_max + b6 * x2_max * \
          x3_max + b7 * x1_max * x2_max * x3_max
    print("Критерій Фішера")
    print(d, " значимих коефіцієнтів")
    f4 = N - d
    sad = ((yy1 - y1_av1) ** 2 + (yy2 - y2_av2) ** 2 + (yy3 - y3_av3) ** 2 + (yy4 - y4_av4) ** 2 + (
            yy5 - y5_av5) ** 2 + (
                   yy6 - y6_av6) ** 2 + (yy7 - y7_av7) ** 2 + (yy8 - y8_av8) ** 2) * (m / (N - d))
    Fp = sad / sb
    print("Fp=", round(Fp, 2))

    Ft = round(abs(f.isf(q, f4, f3)), 4)

    cont = 0
    print("Fp = " + str(round(Fp, 2)) + ", Ft = " + str(Ft))
    if Fp > Ft:
        print("Fp > Ft -> Рівняння неадекватне оригіналу")
        cont = 1
    else:
        print("Fp < Ft -> Рівняння адекватне оригіналу")

