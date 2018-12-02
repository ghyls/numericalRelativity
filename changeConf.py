def changeConf(xmin=2., xmax=16., resolution=2, Nxx=1000, Ntt=20000, \
    every_scalar_t=10, every_aaray_t=100, \
    amplitude=0.1, sigma=1, x0=9., Boundaries=0, Metric=1):

    DEFAULT_xmin=2.
    DEFAULT_xmax=16.
    DEFAULT_resolution=2
    DEFAULT_Nxx=1000
    DEFAULT_Ntt=20000
    DEFAULT_amplitude=0.1
    DEFAULT_x0=9.
    DEFAULT_Boundaries=0
    DEFAULT_Metric=1
    
    conf = open('./input.par','w')
    conf.write('&parameters\n')
    if xmin != '': conf.write('xmin = ' + str(xmin) + '\n')
    else: conf.write('xmin = ' + str(DEFAULT_xmin) + '\n')

    if xmax != '': conf.write('xmax = ' + str(xmax) + '\n')
    else: conf.write('xmax = ' + str(DEFAULT_xmax) + '\n')

    if resolution != '': conf.write('resolution = ' + str(resolution) + '\n')
    else: conf.write('resolution = ' + str(DEFAULT_resolution) + '\n')

    if Nxx != '': conf.write('Nxx = ' + str(Nxx) + '\n')
    else: conf.write('Nxx = ' + str(DEFAULT_Nxx) + '\n')

    if Ntt != '': conf.write('Ntt = ' + str(Ntt) + '\n')
    else: conf.write('Ntt = ' + str(DEFAULT_Ntt) + '\n')

    conf.write('courant = 0.25' + '\n')
    conf.write('every_scalar_t = ' + str(every_scalar_t) + '\n')
    conf.write('every_array_t = ' + str(every_aaray_t) + '\n')

    if amplitude != '': conf.write('amplitude = ' + str(amplitude) + '\n')
    else: conf.write('amplitude = ' + str(DEFAULT_amplitude) + '\n')

    if sigma != '': conf.write('sigma = ' + str(sigma) + '\n')
    else: conf.write('sigma = ' + str(DEFAULT_amplitude) + '\n')

    if x0 != '': conf.write('x0 = ' + str(x0) + '\n')
    else: conf.write('x0 = ' + str(DEFAULT_x0) + '\n')

    if Boundaries != '': conf.write('Boundaries = ' + str(Boundaries) + '\n')
    else: conf.write('Boundaries = ' + str(DEFAULT_Boundaries) + '\n')

    if Metric != '': conf.write('Metric = ' + str(Metric) + '\n')
    else: conf.write('Metric = ' + str(DEFAULT_Metric) + '\n')

    conf.write('/') 
    conf.close()          

    print('-------------------------')

changeConf()