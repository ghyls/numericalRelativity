!! CALCULO DE ONDAS GRAVITACIONALES !! Mario Gonzalez Carpintero ft Diego Valledor Fuertes 

program main

    use global 

    !! PARAMETROS Y VARIABLES !!
    integer Nxx, Ntt                      !variables locales
    integer every_scalar_t, every_array_t !variables locales

    NAMELIST / parameters / xmin, xmax, resolution, Nxx, Ntt, courant, &
                            every_scalar_t, every_array_t, &
                            amplitude, sigma, x0, &
                            Boundaries, Metric

    open(2, file = 'input.par', status = 'old', action = 'read')
    read(2, nml = parameters, IOSTAT = ios)
    close(2)

    pii             = 4.0d0*atan(1.0d0)       !aux
    Nx              = 2**(resolution - 1)*Nxx !divisiones espaciales
    Nt              = 2**(resolution - 1)*Ntt !divisiones temporales
    every_scalar    = 2**(resolution - 1)*every_scalar_t !unidad para guardar escalares
    every_array     = 2**(resolution - 1)*every_array_t  !unidad para guardar arrays
    
    call CPU_TIME(cpu_inicio)
    call principal
    call CPU_TIME(cpu_fin)

    print *
    print *, 'PROGRAM GRAVITATIONAL-WAVE HAS FINISHED'
    print *, 'CPU time has been =', cpu_fin - cpu_inicio
    print *

end program main
