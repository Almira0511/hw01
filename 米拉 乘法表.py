i=9
while i >= 1:
    k=1
    while k <= 9-i:
        print('       ',end='')
        k += 1
    j = 1
    while j <= i:
        print('%d*%d=%-2d'%(i,j,i*j),end=' ')
        j += 1
    print()
    i -= 1