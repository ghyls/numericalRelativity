!! GENERAL EL MALLADO Y CONTROLA QUE LAS SEGNALES NUMERICAS NO SE PROPAGUEN !!

subroutine mesh

    use arrays
    use global

    implicit none

    integer i   !variable de iteracion
    dx = (xmax - xmin)/dble(Nx) !paso espacial
    dt = courant*dx             !paso temporal (las segnales numericas nom se propagan)
    do i = 0, Nx
        x(i) = xmin + dble(i)*dx 
    end do

end subroutine