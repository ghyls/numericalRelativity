###########################
## COMANDOS DE COMPILADO ##
###########################

# 1. Desde la linea de comandos en el mismo directorio que los scripts .f90
# 2. escribir el comando 'make' > se ejecutan los comandos de compilacion
# 3. se habra creado un directorio nuevo llamado '' en la ubicacion del ejecutable Makefile
# 4. ejecutar el archivo '' (con ./nombre o similares) > se crean los archivos '.x' con los datos numericos

#############################################################################################################

# inidcamos el compilador y configuramos el entorno
FC 	   = gfortran
FFLAGS = -O3
LNK    = gfortran

# definimos las subrutinas que queremos compilar en orden de anidado
OBJS = main.o memory.o initial.o mesh.o principal.o save_arrays.o RangKut3.o numeric.o boundaries_calc.o constriction_calc.o
# definimos los modulos
MODS = global.o arrays.o 

#creamos y organizamos los archivos y directorios
all: gravitational-wave 

$(OBJS):	$(MODS)

gravitational-wave:	$(OBJS) $(MODS)
		$(LNK) $(FFLAGS) -o onda $(OBJS) $(MODS) 
	@ mkdir -p COMP 
	@ mv onda COMP 

.PHONY:	clean

clean:
	-rm -f *.o *.mod COMP/onda COMP/*.x COMP/*.tl

%.o : %.f90
	$(FC) -c $(FFLAGS) $< -o $@