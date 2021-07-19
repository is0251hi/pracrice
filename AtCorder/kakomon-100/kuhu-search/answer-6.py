n = int(input())
s = input()
d1 = set()
d2 = set()
d3 = set()
for c in s:
    for t in d2:
        d3.add(t+c)
    for t in d1:
        d2.add(t+c)
    d1.add(c)
print(len(d3))

