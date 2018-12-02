!! MODULO CON LAS VARIABLES SCALARES GLOBALES !!

module global 

    real(kind = 8) pii 
    real(kind = 8) xmin, xmax, dx, courant, t, dt 
    real(kind = 8) amplitude, sigma, x0
    real(kind = 8) cpu_inicio, cpu_fin
    integer resolution
    integer Nx, Nt 
    integer every_scalar
    integer every_array
    integer Boundaries
    integer Metric

end module global