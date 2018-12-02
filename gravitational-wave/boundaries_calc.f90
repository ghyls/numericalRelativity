!! CONTROLA LAS CONDICIONES DE FRONTERA !!

subroutine boundaries_calc

    use arrays
    use global

    implicit none

    !modos R, L y extrapolacion de 2 orden (en la frontera)
    Rmode     = 0.5d0*(Pi - Psi)
    Rmode(0)  = 3.0d0*Rmode(1) - 3.0d0*Rmode(2) + Rmode(3)
    Rmode(Nx) = 3.0d0*Rmode(Nx-1) - 3.0d0*Rmode(Nx-2) + Rmode(Nx-3)
    Lmode     = 0.5d0*(Pi + Psi)
    Lmode(0)  = 3.0d0*Lmode(1) - 3.0d0*Lmode(2) + Lmode(3)
    Lmode(Nx) = 3.0d0*Lmode(Nx-1) - 3.0d0*Lmode(Nx-2) + Lmode(Nx-3)

    !Condiciones de frontera
    if (Boundaries.eq.0) then       !cd. onda saliente
        Psi(0)  = Lmode(0)
        Psi(Nx) = -Rmode(Nx)
        Pi(0)   = Lmode(0)
        Pi(Nx)  = Rmode(Nx)
    else if (Boundaries.eq.1) then  !cd. onda reflexiva
        Psi(0)  = -Psi(1)
        Psi(Nx) = -Psi(Nx-1)
        Pi(0)   = -Pi(1)
        Pi(Nx)  = -Pi(Nx-1)
    else if (Boundaries.eq.2) then  !cd. onda periodica
        Psi(0)  = Psi(Nx-1)
        Psi(Nx) = Psi(1)
        Pi(0)   = Pi(Nx-1)
        Pi(Nx)  = Pi(1)
    else if (Boundaries.eq.3) then  !cd. agujero negro (desaparece)
        Psi(0)  = 3.0d0*Psi(1) - 3.0d0*Psi(2) + Psi(3)
        Psi(Nx) = -Rmode(Nx)
        Pi(0)   = 3.0d0*Pi(1)  - 3.0d0*Pi(2)  + Pi(3)
        Pi(Nx)  = Rmode(Nx)
    else 
        print*, 'NOT IMPLEMENTED YET'
    end if

end subroutine boundaries_calc