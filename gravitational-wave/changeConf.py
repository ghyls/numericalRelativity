def changeConf(xmin=2., xmax=16., resolution=2, Nxx=1000, Ntt=20000, \
            every_scalar_t=10, every_aaray_t=100, \
            amplitud=0.1, sigma=1, x0=9., Boundaries=0, Metric=1):

            conf = open('input.par','w')
            conf.write('&parameters')
            conf.write('xmin = ' + str(xmin) + '\n')
            conf.write('xmax = ' + str(xmax) + '\n')
            conf.write('resolution = ' + str(resolution) + '\n')
            conf.write('Nxx = ' + str(Nxx) + '\n')
            conf.write('Ntt = ' + str(Ntt) + '\n')
            conf.write('courant = 0.25' + '\n')
            conf.write('every_scalar_t = ' + str(every_scalar_t) + '\n')
            conf.write('every_array_t = ' + str(every_aaray_t) + '\n')
            conf.write('amplitud = ' + str(amplitud) + '\n')
            conf.write('sigma = ' + str(sigma) + '\n')
            conf.write('x0 = ' + str(x0) + '\n')
            conf.write('Boundaries = ' + str(Boundaries) + '\n')
            conf.write('Metric = ' + str(Metric) + '\n')
            conf.write('\\') 
            conf.close()          

            print('-------------------------')


