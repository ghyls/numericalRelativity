!! ASIGNACION DE MEMORIA PARA LAS VARIABLES NUMERICAS !!

subroutine memory

    use arrays
    use global

    implicit none

    allocate(x(0:Nx))
    allocate(Phi(0:Nx), Phi_aux(0:Nx), numeric_Phi(0:Nx), dPhi(0:Nx))
    allocate(Psi(0:Nx), Psi_aux(0:Nx), numeric_Psi(0:Nx), dPsi(0:Nx))
    allocate(Pi(0:Nx), Pi_aux(0:Nx), numeric_Pi(0:Nx), dPi(0:Nx))
    allocate(Lmode(0:Nx), Rmode(0:Nx))
    allocate(alpha(0:Nx), dalpha(0:Nx))
    allocate(beta(0:Nx), dbeta(0:Nx))
    allocate(gamma(0:Nx), dgamma(0:Nx))
    allocate(gamma_rr(0:Nx), dgamma_rr(0:Nx))
    allocate(constriction(0:Nx))

end subroutine memory