subroutine constriction_calc

    use arrays
    use global

    implicit none

    integer i           !variable de iteracion
    real(kind = 8) idx  !aux

    !calculamos la condicion de ligadura inicial derivando Psi respecto a las coordenadas
    idx = 1.0d0/dx  !mas eficiente en cada iteracion
    !Derivada centrada 
    do i = 1, Nx-1
        dPhi(i) = 0.5d0*(Phi(i+1) - Phi(i-1)*idx)
    end do
    !Derivadas laterales
    dPhi(0)  = 0.5d0*(-3.0d0*Phi(0) + 4.0d0*Phi(1)    - Phi(2))*idx
    dPhi(Nx) = 0.5d0*(3.0d0*Phi(Nx) - 4.0d0*Phi(Nx-1) + Phi(Nx-2))*idx
    
    constriction = Psi - dPhi

end subroutine constriction_calc