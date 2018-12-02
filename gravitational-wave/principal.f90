!! SUBRUTINA PRINCIPAL, CONTROLA LAS RUTINAS DE CALCULO NUMERICO Y LAS DE GENERACION DE ARCHIVOS !!

subroutine principal

    use arrays
    use global

    implicit none
    integer l   !variable de iteracion

    call memory !asignacion de memoria

    print *
    print *, '... Memory asignament completed'
    print *

    call mesh   !asignacion de memoria

    print *
    print *, '... Meshing completed'
    print *

    !inicializamos variables (aux)
    t       = 0
    Phi_aux = 0.0d0
    Psi_aux = 0.0d0
    Phi_aux = 0.0d0 

    call initial    !proporciona las cantidades derivadas de los parametros del programa

    print *
    print *, '... Constriction condition calculated'
    print *

    call save_arrays(Phi, 'Phi', 0)
    call save_arrays(Psi, 'Psi', 0)
    call save_arrays(Pi, 'Pi', 0)
    call save_arrays(alpha, 'alpha', 0)
    call save_arrays(beta, 'beta', 0)
    call save_arrays(constriction, 'constriction', 0)

    !agregamos daots al archivo de salida
    do l = 1, Nt
        
        t = t + dt 
        call RangKut3   !inicia los calculos numericos

        if (mod(l, every_array).eq.0) then
            call save_arrays(Phi, 'Phi', 1)
            call save_arrays(Psi, 'Psi', 1)
            call save_arrays(Pi, 'Pi', 1)
            call save_arrays(constriction, 'constriction', 1)
        end if 

    end do
    print *
    print *, '... Numerical fields calculated'
    print *

    print *
    print *, 'Saving data ...'
    print *

end subroutine principal