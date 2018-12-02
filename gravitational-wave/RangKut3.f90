subroutine RangKut3

    use arrays
    use global

    implicit none

    integer k               !variable de iteracion
    real(kind = 8) dt_aux   !aux

    !guardamos el valor anterior de los campos
    Phi_aux = Phi
    Psi_aux = Psi 
    Pi_aux  = Pi 

    !arrancamos el metodo, los coeficientes de RK estan previamente calculados
    do k = 1, 3
        call numeric    !calculo las derivadas de los campos segun los parametros de entrada
        
        if (k.eq.1) then
            dt_aux = dt
            Phi = Phi_aux + dt_aux*numeric_Phi
            Psi = Psi_aux + dt_aux*numeric_Psi
            pi  = Pi_aux  + dt_aux*numeric_Pi
        else if (k.eq.2) then
            dt_aux = 0.25d0*dt 
            Phi = 0.75d0*Phi_aux + 0.25d0*Phi + dt_aux*numeric_Phi 
            Psi = 0.75d0*Psi_aux + 0.25d0*Psi + dt_aux*numeric_Psi 
            Pi  = 0.75d0*Pi_aux  + 0.25d0*Pi  + dt_aux*numeric_Pi 
        else
            dt_aux = 2.0d0*dt/3.0d0
            Phi = (Phi_aux + 2.0d0*Phi)/3.0d0 + dt_aux*numeric_Phi 
            Psi = (Psi_aux + 2.0d0*Psi)/3.0d0 + dt_aux*numeric_Psi 
            Pi  = (pi_aux  + 2.0d0*Pi)/3.0d0  + dt_aux*numeric_Pi 
        end if
    end do

    call boundaries_calc    !condiciones de frontera
    call constriction_calc  !actualiza condiciones de ligadura 

end subroutine RangKut3