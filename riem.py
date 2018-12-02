import sympy as sp
from christ import christoffel


def riemman(ds, g_mn, abcd):
    
    # calcula R^a_{bcd}
    # ds se refiere al orden de las variabels en el intervalo
    # g_mn es la métrica
    # abcd = los índices de la componente de R que queremos calcular


    orden = []
    for i, e in enumerate(ds):
        #str -> sym
        if e != '': 
            exec("var"+str(i)+"=sp.symbols('"+e+"')")
            exec("orden.append(var"+str(i)+")")


    # Creamos un array con los índices de los símbolos de Christoffel
    # \Gamma_ab^c que quedemos calcular, 
    ABC = []

    # R^a_{bcd} tiene cuatro términos. Para cada término,
    ABC.append([abcd[3],  abcd[1],  abcd[0]])   #t1
    ABC.append([abcd[2],  abcd[1],  abcd[0]])   #t2
    for i in range(len(ds)):
        ABC += [[abcd[2], ds[i], abcd[0]], [abcd[3], abcd[1], ds[i]]]    #t3
        ABC += [[abcd[3], ds[i], abcd[0]], [abcd[2], abcd[1], ds[i]]]    #t4

    symbols = christoffel(ds, g_mn, ABC=ABC)
    
    # cada termino de la expresión de R:
    
    r1 = sp.diff(symbols[0], abcd[2])
    r2 = sp.diff(symbols[1], abcd[3])
    r3 = r4 = 0

    i = 2   #rellenamos r3 y r4    
    while i < len(symbols):
        r3 += symbols[i] * symbols[i+1]
        i += 2
        r4 += symbols[i] * symbols[i+1]
        i += 2
        


    S = sp.simplify(r1 - r2 + r3 - r4)   #esto es R^a_{bcd}


    return(S)
    
    

'''
abcd = ["t", "r", "t", "r"]
ds = ['t', 'r', 'th', 'fi']
g_mn = [['-(1-2*G*M/r)', '', '', ''], ['', '1/(1-2*G*M/r)', '', ''], ['', '', 'r**2', ''], ['', '', '', 'r**2*sin(th)**2']]

R = riemman(ds, g_mn, abcd)
print(R)
R.subs('t', 'th')
print(R)
'''
