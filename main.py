def dl(x1, y1, x2, y2):
    return ( (x1 - x2)**2 + (y1 - y2)**2 )**0.5

def isk(a):
    mins = 10**10
    for i in range(len(a)):
        mas = [1000]*10
        x1 = a[i][0]
        y1 = a[i][1]
        for j in range(len(a)):
            x2 = a[j][0]
            y2 = a[j][1]
            ts = dl(x1, y1, x2, y2)
            if j == i:
                continue
            for k in range(len(mas)):
                max_el = max(mas)
                max_el_ind = mas.index(max_el)
                if mas[max_el_ind] > ts:
                    mas[max_el_ind] = ts
        if sum(mas) < mins:
            mins = sum(mas)
            res = a[i]
    return res

f = open("27_A_custom.txt")
a1, a2 = [], []
for s in f:
    s = s.replace(',', '.')
    a = [float(x) for x in s.split()]
    x = a[0]
    y = a[1]
    if y < 5:
        a1.append(a)
    else: a2.append(a)

res1 = isk(a1)
res2 = isk(a2)

print((res1[0]+res2[0])/2*10000)
print((res1[1]+res2[1])/2*10000)

f = open("27_B_custom.txt")
a1, a2, a3 = [], [], []
for s in f:
    s = s.replace(',', '.')
    a = [float(x) for x in s.split()]
    x = a[0]
    y = a[1]
    if y < 4 - x:
        a1.append(a)
    elif (y > 4 - x) and (y < (-1.5*x + 15)):
        a2.append(a)
    else: a3.append(a)

res1 = isk(a1)
res2 = isk(a2)
res3 = isk(a3)

print((res1[0] + res2[0] + res3[0])/3*10000)
print((res1[1] + res2[1] + res3[1])/3*10000)
