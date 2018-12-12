import collections
a = []
with open('first_five') as f:
    for i in f:
        i = i.strip('\n')
        a.append(i)
        b = list(a)
    c = collections.Counter(b)
with open('FirstFiveResult', 'w') as g:
    for i in c:
        g.write(i + '\t' + str(c[i]) + '\n')