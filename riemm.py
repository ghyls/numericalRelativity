import sympy as sp
from christ import christoffel


def riemman(ds, g_mn, abcd):

    #calcula R_{abcd}

    orden = []
    for i, e in enumerate(ds):
        #str -> sym
        if e != '': 
            exec("var"+str(i)+"=sp.symbols('"+e+"')")
            exec("orden.append(var"+str(i)+")")

    # cada termino de la expresión de R:
    t1 = sp.diff(christoffel(ds, g_mn, [abcd[3], abcd[1], abcd[0]]), abcd[2])
    t2 = sp.diff(christoffel(ds, g_mn, [abcd[2], abcd[1], abcd[0]]), abcd[3])

    t3 = 0
    for i in range(len(ds)):
        t3 += christoffel(ds, g_mn, [abcd[2], ds[i], abcd[0]])* \
              christoffel(ds, g_mn, [abcd[3], abcd[1], ds[i]])
    t4 = 0
    for i in range(len(ds)):
        t4 += christoffel(ds, g_mn, [abcd[3], ds[i], abcd[0]])* \
              christoffel(ds, g_mn, [abcd[2], abcd[1], ds[i]])
    
    R = sp.simplify(t1 + t2 + t3 + t4)   #esto es R^a_{bcd}

    '''
    RD = 0  #esto es R_{abcd}
    for i in range(len(ds)):
        RD += g_mn[abcd[0]][i] * 
    '''
    return(R)
    
    


abcd = ["t", "r", "t", "th"]
ds = ['t', 'r', 'th', 'fi']
g_mn = [['-(1-2*G*M/r)', '', '', ''], ['', '1/(1-2*G*M/r)', '', ''], ['', '', 'r**2', ''], ['', '', '', 'r**2*sin(th)**2']]

print(riemman(ds, g_mn, abcd))

