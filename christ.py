import sympy as sp

def christoffel(ds, g_mn, abc = [], ABC = []):

    # ds contiene el orden de las variables en el intervalo
    # g_mn es la métrica, en forma de 2D tupla

    # calcula \Gamma_{ab}^c. 
    
    # ABC contiene múltiples tuplas abc. Se usa para calcular varios símbolos
    # en una sola llamada.

    #Constantes que podrían aparecer en la métrica
    G, M, R, C1, C2, C3 = sp.symbols('G M R C1 C2 C3')
    
    
    orden = [] #el orden en el que aparecen las variables de la meteica
    
    for i, e in enumerate(ds):
        #Las variables de la métrica
        if e != '': 
            exec("var"+str(i)+"=sp.symbols('"+e+"')")
            exec("orden.append(var"+str(i)+")")

    ordenSt = [str(k) for k in orden]
    d = len(ordenSt)

    #la métrica con los íncices a b abajo
    gabD = sp.zeros(d, d)
    for i, row in enumerate(g_mn):
        for j, elem in enumerate(row):
            if i >= d or j >= d: continue
            if elem != '': gabD[i,j] = elem
            else: gabD[i,j] = 0

    #y con los índices arriba, 
    gabU = gabD.inv()

    gabD = gabD.tolist()
    gabU = gabU.tolist()



    if ABC == [] and abc != []:
        #Vamos a calcular solo el símbolo \Gamma_{ab}^c
        a = abc[0]
        b = abc[1]
        c = abc[2]

        ai = ordenSt.index(a)
        bi = ordenSt.index(b)
        ci = ordenSt.index(c)

        chrst = 0
        
        for di in range(len(gabD)):
            chrst += 1./2*gabU[ci][di]*(sp.diff(gabD[bi][di], ordenSt[ai]) + sp.diff(gabD[di][ai], ordenSt[bi]) - sp.diff(gabD[ai][bi], ordenSt[di]))
        
        return(chrst)
    

    elif ABC != [] and abc == []:
        #vamos a calcular varios símbolos de una sola vez
        CHRIST = [] 

        for elem in ABC:
            a = elem[0]
            b = elem[1]
            c = elem[2]  

            ai = ordenSt.index(a)
            bi = ordenSt.index(b)
            ci = ordenSt.index(c)
            chrst = 0
            for di in range(len(gabD)):
                chrst += 1./2*gabU[ci][di]*(sp.diff(gabD[bi][di], ordenSt[ai]) + sp.diff(gabD[di][ai], ordenSt[bi]) - sp.diff(gabD[ai][bi], ordenSt[di]))
            CHRIST.append(chrst)
        
        return CHRIST
    else: print("wrong call! either abc or ABC must be empty")

    


'''
abc = ["r", "t", "t"]
ds = ['t', 'r', 'th', 'fi']
g_mn = [['-(1-2*G*M/r)', '', '', ''], ['', '1/(1-2*G*M/r)', '', ''], ['', '', 'r**2', ''], ['', '', '', 'r**2*sin(th)**2']]
print(christoffel(ds, g_mn, abc))
'''