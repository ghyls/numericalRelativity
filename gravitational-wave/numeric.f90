!! CALCULO NUMERICO DE LAS DERIVADAS DE LOS CAMPOS !!

subroutine numeric 

    use arrays
    use global

    implicit none

    integer i          !variable de iteracion
    real(kind = 8) idx !aux

    !calculo numerico por diferencias finitas (derivadas de 2 orden)
    idx = 1.0d0/dx !mas eficiente en cada iteracion
    !derivadas centradas
    do i = 1, Nx-1
        dPsi(i) = 0.5d0*(Psi(i+1) - Psi(i-1))*idx 
        dPi(i)  = 0.5d0*(Pi(i+1) - Pi(i-1))*idx
    end do
    !derivadas laterales
    dPsi(0)  = 0.5d0*(-3.0d0*Psi(0) + 4.0d0*Psi(1) - Psi(2))*idx
    dPsi(Nx) = 0.5d0*(3.0d0*Psi(Nx) - 4.0d0*Psi(Nx-1) + Psi(Nx-2))*idx 
    dPi(0)   = 0.5d0*(-3.0d0*Pi(0)  + 4.0d0*Pi(1)  - Pi(2))*idx
    dPi(Nx)  = 0.5d0*(3.0d0*Pi(Nx)  - 4.0d0*Pi(Nx-1)  + Pi(Nx-2))*idx 

    !valores numericos segun la metrica
    if (Metric.eq.0) then       !Mink
        numeric_Phi = Pi 
        numeric_Psi = dPi 
        numeric_Pi  = dPsi
    else if (Metric.eq.1) then  !Schwar   
        numeric_Phi = alpha*Pi + beta*Psi 
        numeric_Psi = alpha*dPi + dalpha*Pi + beta*dPsi + dbeta*Psi 
        numeric_Pi  = dgamma*(beta*Pi + alpha*gamma_rr*Psi)/gamma &
        + beta*dPi + dbeta*Pi + dalpha*gamma_rr*dPsi &
        + alpha*dgamma_rr*Psi + alpha*gamma_rr*dPsi
    else
        print *, 'METRIC NO IMPLEMENTED YET'
    end if

end subroutine numeric 