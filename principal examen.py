import funciones as fn 

alumnos = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
    "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
    ]
creditos_alumnos={}

while True:
    print("         MENU        ")
    print("*********************")
    print("0. Inicializa creditos")
    print("1. Asignar creditos")
    print("2. Clasificacion de Creditos")
    print("3. Calculo de Estadisticas de creditos ")
    print("4. Generacion de reportes")
    print("5. Salir")
    opcion= int(input("Seleccione una opcion: "))
    if opcion == 0 :
        creditos_alumnos = {alumno : 0 for alumno in alumnos}
        print("Creditos inicializados")
    elif opcion == 1 :
        if not creditos_alumnos :
            print("Debe inicializar creditos")
        else : 
            creditos_alumnos = fn.asignar_creditos(alumnos)
    elif opcion== 2 :
        if creditos_alumnos:
            fn.clasificacion_creditos(creditos_alumnos)
        else :
            print("debe asignar creditos")
    elif opcion == 3 :
        if creditos_alumnos :
            max_creditos,min_creditos,promedio_creditos = fn.calcular_estadisticas(creditos_alumnos)
            if max_creditos is not  None:
                print("Credito minimo es: ",min_creditos)
                print("Credito maximo es: ",max_creditos)
                print("Credito promedio es: ",promedio_creditos)
            else:
                print("Debe asignar creditos")
    elif opcion == 4:
        if creditos_alumnos:
            menor_100, entre_100_150, mayor150 = fn.clasificacion_creditos(creditos_alumnos)
            # Generar reporte usando los datos clasificados
            fn.generar_reporte(creditos_alumnos, menor_100, entre_100_150, mayor150)
        else:
            print("Debe generar creditos")
    elif opcion == 5 :
        print("Saliendo.....")
        break
    else:
        print("Debe seleccionar una opcion entre el 0 y el 5")