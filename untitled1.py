def tablize(n, truths=[]):
    if not n:
        print (truths)
    else:
        for i in [True, False]:
            tablize(n-1, truths+[i])


for p in False, True:
    for q in False, True:
        for r in False, True:
            print ('|{} | {} | {} |'.format(p,q, r))
            
tablize(3)
            
