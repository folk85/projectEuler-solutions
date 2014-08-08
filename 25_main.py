n = 100
p = [0]*n
#print p[1][:], len(p[0][:]), 13//5
pv = [0]*n
ppv = [0]*n
magn = 10**10
#p[0][0] = 1
#p[1][0] = 1
pv[0] = 1
ppv[0] = 1
i_num = 2
while (p[-1] < 1 ):
    for i in xrange(n):
        p[i] = pv[i] + ppv[i]
    for i in xrange(n):
#        print i,p[i],pv[i],ppv[i], p[i]>=magn
        if (pv[i] < magn and p[i] >= magn):
            val = (p[i] // magn)
            p[i] -= val * magn
            p[i+1] += val
        ppv[i] = pv[i]
        pv[i] = p[i]
    i_num += 1
#    print i_num, p[-1], p[0]
#    if (i_num > 15):
#        break
print i_num
