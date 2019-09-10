import sympy as sp


def christoffel(ds, g_mn, abc = [], ABC = []):

    # ds contiene el orden de las variables en el intervalo
    # g_mn es la métrica, en forma de 2D tupla

    # calcula \Gamma_{ab}^c. 
    
    # ABC contiene múltiples tuplas abc. Se usa para calcular varios símbolos
    # en una sola llamada.

    #Constantes que podrían aparecer en la métrica
    #G, M, R, C1, C2, C3 = sp.symbols('G M R C1 C2 C3')
    
    
    orden = [] #el orden en el que aparecen las variables de la meteica
    
    for i, e in enumerate(ds):
        #Las variables de la métrica
        if e != '': 
            exec("var"+str(i)+"=sp.symbols('"+e+"')")
            exec("orden.append(var"+str(i)+")")

    ordenSt = [str(k) for k in orden]

    # chack the dimension of g_mn
    dim = 0
    if all(k.strip() == "" for k in g_mn[3][:]) and all(k[3].strip() == "" for k in g_mn[:][:4]):
        if all(k.strip() == "" for k in g_mn[2][:3]) and all(k[2].strip() == "" for k in g_mn[:][:3]):
            if all(k.strip() == "" for k in g_mn[1][:1]) and all(k[1].strip() == "" for k in g_mn[:][:2]):
                dim = 1
            else: dim = 2
        else: dim = 3
    else: dim = 4
    #la métrica con los íncices a b abajo
    gabD = sp.zeros(dim, dim)
    
    for i, row in enumerate(g_mn[:dim]):
        for j, elem in enumerate(row[:dim]):
            if i >= dim or j >= dim: continue
            try:
                if elem.strip() != '': gabD[i,j] = elem
            except Exception as e:
                error = "syntaxError"
                return [error, i, j]

    #y con los índices arriba, 
    try:
        gabU = gabD.inv()
    except:
        error = "matrixNonInv"
        return [error]
    


    dsElemCount = 0
    
    for k in ds:
        if str(k).strip() != "": dsElemCount += 1 

    if dsElemCount != dim:
        error = "dimMismatch"
        return [error]

    gabD = gabD.tolist()
    gabU = gabU.tolist()



    if ABC == [] and abc != []:
        #Vamos a calcular solo el símbolo \Gamma_{ab}^c
        a = abc[0]
        b = abc[1]
        c = abc[2]

        try: ai = ordenSt.index(a)
        except: error = "unknownVar"; return([error, a])

        try: bi = ordenSt.index(b)
        except: error = "unknownVar"; return([error, b])

        try: ci = ordenSt.index(c)
        except: error = "unknownVar"; return([error, c])            

        chrst = 0
        
        for di in range(dim):
            chrst += 1./2*gabU[ci][di]*(sp.diff(gabD[bi][di], ordenSt[ai]) + sp.diff(gabD[di][ai], ordenSt[bi]) - sp.diff(gabD[ai][bi], ordenSt[di]))
        
        #sp.pprint(Integral(sqrt(1/x), x), use_unicode=False)

        return([chrst])
    

    elif ABC != [] and abc == []:
        #vamos a calcular varios símbolos de una sola vez
        CHRIST = [] 

        for elem in ABC:
            a = elem[0]
            b = elem[1]
            c = elem[2]  

            try: ai = ordenSt.index(a)
            except: error = "unknownVar"; return([error, a])
            try: bi = ordenSt.index(b)
            except: error = "unknownVar"; return([error, b])
            try: ci = ordenSt.index(c)
            except: error = "unknownVar"; return([error, c])  

            chrst = 0
            for di in range(len(gabD)):
                chrst += 1./2*gabU[ci][di]*(sp.diff(gabD[bi][di], ordenSt[ai]) + sp.diff(gabD[di][ai], ordenSt[bi]) - sp.diff(gabD[ai][bi], ordenSt[di]))
            CHRIST.append(chrst)
        
        return [CHRIST]
    else: print("wrong call! either abc or ABC must be empty")

    



#abc = ["fi", "r", "fi"]
#ds = ['t', 'r', 'th', 'fi']
#g_mn = [['-(1-2*G*M/r)', '', '', ''], ['', '1/(1-2*G*M/r)', '', ''], ['', '', 'r**2', ''], ['', '', '', 'r**2*sin(th)**2']]

#print("Γ")
#sp.pprint(christoffel(ds, g_mn, abc))
