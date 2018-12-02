!! MODULO CON VARIABLES Y ARREGLOS DIMENSIONALES !!

module arrays

    implicit none

    real(kind = 8), allocatable, dimension (:) :: x 
    real(kind = 8), allocatable, dimension (:) :: Phi, Phi_aux, numeric_Phi, dPhi
    real(kind = 8), allocatable, dimension (:) :: Psi, Psi_aux, numeric_Psi, dPsi
    real(kind = 8), allocatable, dimension (:) :: Pi, Pi_aux, numeric_Pi, dPi
    real(kind = 8), allocatable, dimension (:) :: Lmode, Rmode
    real(kind = 8), allocatable, dimension (:) :: alpha, dalpha
    real(kind = 8), allocatable, dimension (:) :: beta, dbeta
    real(kind = 8), allocatable, dimension (:) :: gamma, dgamma
    real(kind = 8), allocatable, dimension (:) :: gamma_rr, dgamma_rr
    real(kind = 8), allocatable, dimension (:) :: constriction

end module arrays