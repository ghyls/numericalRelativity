!! CANTIDADES DERIVADAS DE LOS PARAMETROS DEL PROGRAMA !!

subroutine initial

    use arrays
    use global

    implicit none

    !cantidades derivadas de la metrica de Schwar
    alpha       = 1.0d0/sqrt(1.0d0 + 2.0d0/x)
    dalpha      = 1.0d0/(x**2*(1.0d0 + 2.0d0/x)**(3.0d0/2.0d0))
    beta        = 2.0d0/(x*(1.0d0 + 2.0d0/x))
    dbeta       = -2.0d0/(2.0d0 + x)**2.0d0 
    gamma       = sqrt(x**4*(1.0d0 + 2.0d0/x))
    dgamma      = (x**2*(3.0d0 + 2.0d0*x))/sqrt(x**3*(2.0d0 + x))
    gamma_rr    = 1.0d0 + 2.0d0/x 
    dgamma_rr   = -2.0d0/x**2

    !campos 
    Phi         = amplitude*exp(-(x-x0)**2/sigma**2)
    Psi         = -2.0d0*Phi*((x-x0)/sigma**2)
    Pi          = 0.0d0

    call constriction_calc   !resolvemos las ecs. de ligadura

end subroutine initial