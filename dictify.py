def mcqdictfy(string):
    y = string
     #looping through the number of questions OR statement to handle two scenario
    for x in [1,2,3,4,5,6,7,8,9,10]:
        y = y.replace(str(x)+"." or str(x)+". ", '''"]},{'''+str(x)+":["+'"Q-'+str(x)+". ",2)
    # looping through the options
    for k in ['(a)','(b)','(c)','(d)']:
        y = y.replace(k, '","'+k)
    y = y +'"]}]'
    return y 


def mcqfy(string):
    a = list(mcqdictfy(string))
    del a[0:4]
    f = "["+"".join(a)
    return f
