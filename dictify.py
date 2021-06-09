def mcqdictfy(string):
    y = string
    for x in [1,2,3,4,5,6,7,8,9,10]:
        y = y.replace(str(x)+". ", " ']},{' "+str(x)+":["+'"Q-'+str(x)+". ",2)
    for k in ['(a)','(b)','(c)','(d)']:
        y = y.replace(k, '","'+k)
    y = y +'"]}]'
    y = y.replace(y[0:4],"[")
    return y
