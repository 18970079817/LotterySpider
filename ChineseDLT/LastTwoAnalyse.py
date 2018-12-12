import collections
a = []
with open('last_two') as f:
    for i in f:
        i = i.strip('\n')
        a.append(i)
        b = list(a)
    c = collections.Counter(b)
with open('LastTwoResult', 'w') as g:
    for i in c:
        g.write(i + '\t' + str(c[i]) + '\n')