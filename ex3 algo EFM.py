t = []

for i in range(0, 9):
    n = float(input("Type the number: "))
    t.append(n)

s = t[0] + t[1] + t[2] + t[3]
u = 0

for i in range(1, 6):
    k = t[i] + t[i + 1] + t[i + 2] + t[i + 3]
    
    if k > s:
        s = k
        u = i

print("The maximum sum is [", t[u], ",", t[u + 1], ",", t[u + 2], ",", t[u + 3], "] with a sum of", s)