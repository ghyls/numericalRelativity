subroutine save_arrays(fval, base_name, first_index)
    !fval: variable que queremos guardar en el archivo (numerica)
    !base_name: nombre de entrada de la variable anterior
    !first_index: controla el flujo de datos (evitar datos repetidos, por ejemplo tras una nueva ejecucion)

    use arrays 
    use global 

    implicit none

    integer i, first_index !variables de iteracion/aux

    !configuramos variables del archivo
    character(len = 20) filestatus       !estado del archivo
    character(len = 256) :: filename    !nombre del archivo
    logical firstcall
    data firstcall / .true. /
    save firstcall

    !definimos los argumentos de la subrutina
    character(len = *), intent(IN) :: base_name         
    real(kind = 8), dimension(0:Nx), intent(IN) :: fval
    
    !extension de los archivos (.x para modelos tridimensionales futuros)
    if (resolution.eq.1) then
        filename = base_name // '1_.x'  !el subindice indica la resolucion del mallado
    else if (resolution.eq.2) then
        filename = base_name // '_2.x'
    else if (resolution.eq.3) then
        filename = base_name // '_3.x'
    else if (resolution.eq.4) then
        filename = base_name // '_4.x'
    else if (resolution.eq.5) then
        filename = base_name // '_5.x'
    end if

    !controlamos el flujo de datos
    if (first_index.eq.0) then  !primera ejecucion > comienza desde cero
        filestatus = 'replace'
    else
        filestatus = 'old'      !ejecucion posterior > agrega elementos
    end if

    !guardamos los datos de salida
    if (filestatus == 'replace') then
        open(1, file = filename, form = 'formatted', status = filestatus)
    else
        open(1, file = filename, form = 'formatted', status = filestatus, position = 'append')
    end if

    write(1,*) ''
    write(1,*) '#Time = ', t
    do i = 0, Nx, 2**(resolution-1)
        write(1,*) x(i), fval(i)
    end do
    write(1,*)
    close(1)

end subroutine save_arrays 