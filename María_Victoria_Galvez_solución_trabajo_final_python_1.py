

def cargaDeDatos():
    socios_a_cargar = int(input("¿Cántos socios va a cargar?: "))
    socios = []
    legajos = []

    for x in range (socios_a_cargar):
        nombre = input("Ingrese el nombre del socio: ")
        while len(nombre) == 0:
            print("Error, no ingreso un nombre")
            nombre = input("Ingrese un nombre: ")
        
        apellido = input("Ingrese el apellido del socio: ")
        while len(apellido) == 0:
            print("Error, no ingreso un apellido")
            apellido = input("Ingrese un apellido: ")
        
        legajo = int(input("Ingrese el legajo: "))

        while legajo in legajos:
            legajo_alternativo = legajo + 1
            legajo = legajo_alternativo
        legajos.append(legajo)
        
        telefono = int(input("Ingrese su teléfono: "))

        mail = input("Ingrese su mail: ")
        
        situacion_socio = input("¿El socio esta al día con las cuotas? [si / no]:  ")
        al_dia = "si"
        debe = "no"
        si = False
        while situacion_socio != al_dia and situacion_socio != debe:
            print("Error!")
            situacion_socio = input("¿El socio esta al día con las cuotas? [si / no]:  ")
        if situacion_socio == al_dia:
            si= True
            situacion_socio = "al día"
        elif situacion_socio == debe:
            si = False
            situacion_socio = "debe la última cuota"

        condicion = input("ingrese la condición: ")
        condicion_p = "premium"
        condicion_e = "estandar"
        premium = False
        while condicion != condicion_p and condicion != condicion_e:
            print("Error!")
            condicion = input("ingrese la condición: ")
        if condicion == condicion_p:
            premium = True
            condicion = condicion_p
        elif condicion == condicion_e:
            premium = False
            condicion = condicion_e
        
        socio = [nombre , apellido, legajo, telefono, mail, situacion_socio, condicion]
        socios.append(socio)
        
    return socios


def mostrar_datos(DATOS):
    for x in range (len(DATOS)):
        print(f"---Datos del socio ---")
        print(f"Nombre: {DATOS[x][0]} - Apellido: {DATOS[x][1]} ")
        print(f"Legajo: {DATOS[x][2]}")
        print(f"Telefono: {DATOS[x][3]}")
        print(f"Mail: {DATOS[x][4]}")
        print(f"Situación actual: {DATOS[x][5]}")
        print(f"Condición: {DATOS[x][6].upper()}")
        print("-----------------------------------")
        

def legajos_ordenados(DATOS):   
    for x in range (len(DATOS)):
        datos_ordenados = sorted(DATOS, key=lambda socio: socio[2])
        print(f"---Datos del socio ---")
        print(f"Nombre: {datos_ordenados[x][0]} - Apellido: {datos_ordenados[x][1]} ")
        print(f"Legajo: {datos_ordenados[x][2]}")
        print(f"Telefono: {datos_ordenados[x][3]}")
        print(f"Mail: {datos_ordenados[x][4]}")
        print(f"Situación actual: {datos_ordenados[x][5]}")
        print(f"Condición: {datos_ordenados[x][6].upper()}")
        print("-----------------------------------")

def cambiar_condicion(DATOS):
    socio_a_cambiar = int(input("Ingrese el legajo del socio a cambiar: "))
    for x in range (len(DATOS)):
        if socio_a_cambiar == DATOS[x][2]:
            print(f"{DATOS[x][0]} {DATOS[x][1]} es socio/a {DATOS[x][6].upper()} del club")
            cambio_condicion = input("¿Desea cambiar esta condición?: [si/no]: ")
            cambio = "si"
            no_cambio = "no"
            si = False
            while cambio_condicion != cambio and cambio_condicion != no_cambio:
                print("Respuesta no válida")
                cambio_condicion = input("¿Desea cambiar esta condición?: [si/no]: ")
            if cambio_condicion == cambio:
                si = True
                condicion_nueva = input("Ingrese la nueva condición: ")
                condicion_p = "premium"
                condicion_e = "estandar"
                premium = False
                while condicion_nueva != condicion_p and condicion_nueva != condicion_e:
                    print("Respuesta no válida")
                    condicion_nueva = input("Ingrese la nueva condición: ")
                if condicion_nueva == condicion_p:
                    premium = True
                    condicion_nueva = condicion_p
                elif condicion_nueva == condicion_e:
                    premium = False
                    condicion_nueva = condicion_e
                DATOS[x][6] = DATOS[x][6].replace(DATOS[x][6], condicion_nueva)
                print(f"{DATOS[x][0]} {DATOS[x][1]} ahora es socio/a {DATOS[x][6].upper()} del club")

            elif cambio_condicion == no_cambio:
                si = False
    return DATOS
    



def dar_baja(DATOS):
    socio_a_dar_baja = int(input("Ingrese el legajo del socio que quiere dar de baja: "))
    x = 0 
    while x < len(DATOS):
        if socio_a_dar_baja == DATOS[x][2]:
            print(f"El legajo {DATOS[x][2]} corresponde al socio {DATOS[x][0]} {DATOS[x][1]}")
            baja = input("¿Desea dar de baja?: [si/no]: ")
            baja_si = "si"
            baja_no = "no"
            si = False
            while baja != baja_si and baja != baja_no:
                print("Respuesta no válida")
                baja = input("¿Desea dar de baja?: [si/no]: ")
            if baja == baja_si:
                si = True
                print(f"El socio {DATOS[x][0]} {DATOS[x][1]} fue dado de baja")
                DATOS.remove(DATOS[x])
            elif baja == baja_no:
                si = False
        x += 1
    return DATOS
            

def recaudacion_actual(DATOS):
    socios_al_dia_p = 0
    socios_al_dia_e = 0
    socios_deben_p = 0
    socios_deben_e = 0
    for x in range(len(DATOS)):
        if DATOS[x][5] == "al día" and DATOS[x][6] == "premium" :
            socios_al_dia_p += 1
        elif DATOS[x][5] == "debe la última cuota" and DATOS[x][6] == "premium":
            socios_deben_p +=1
        elif DATOS[x][5] == "al día" and DATOS[x][6] == "estandar" :
            socios_al_dia_e += 1 
        elif DATOS[x][5] == "debe la última cuota" and DATOS[x][6] == "estandar" :
            socios_deben_e += 1 

    print(f"El club cuenta actualmente con {socios_al_dia_p} socios premium al día y {socios_al_dia_e} socios estandar al día, lo que da una recaudación actual de ${(socios_al_dia_p * 5800)+ (socios_al_dia_e * 1800)}.")
    print(f"El club cuenta actualmente con {socios_deben_p} socio premium con deuda y {socios_deben_e} socios estandar con deuda, lo que significa que al club le faltan ${(socios_deben_p * 5800)+(socios_deben_e * 1800)} por recaudar")

def recaudacion(DATOS):
    socios_premium = 0
    socios_estandar = 0
    for x in range(len(DATOS)):
        if DATOS[x][6] == "premium" :
            socios_premium += 1
        elif DATOS[x][6] == "estandar":
            socios_estandar +=1
    recaudacion_premium = socios_premium * 5800
    recaudacion_estandar = socios_estandar * 1800
    recaudacion_mensual = recaudacion_premium + recaudacion_estandar
    recaudacion_anual =  recaudacion_mensual * 12
    print("--------- Informe de Recaudación -------------")
    print("---------- Informe de Socios --------------")
    print("PREMIUM:")
    print("Los socios PREMIUM tienen un abono mensual de $5800.")
    print(f"El club cuenta con {socios_premium} socios en condición PREMIUM.")
    print(f"El club recauda ${recaudacion_premium} con sus socios PREMIUM.")
    print("ESTANDAR:")
    print("Los socios ESTANDAR tienen un abono mensual de $1800.")
    print(f"El club cuanta con {socios_estandar} socios en condición ESTANDAR.")
    print(f"El club reacuada ${recaudacion_estandar} con sus socios ESTANDAR.")
    print("-------------------")
    print(f"Recaudación mensual final ${recaudacion_mensual} ")
    print(f"Recaudación anual final ${recaudacion_anual} ")
    print("-------------------")
    print("Apreciación final:")
    objetivo_anual = int(input("Ingrese el objetivo anual: $"))
    if objetivo_anual < recaudacion_anual:
        print(f"Siendo ${objetivo_anual} el objetivo anual de recaudación del club y ${recaudacion_anual} la recaudación final obtenida , el objetivo anual de recaudación se consiguió.")
    elif objetivo_anual > recaudacion_anual:
        print(f"Siendo ${objetivo_anual} el objetivo anual de recaudación del club y ${recaudacion_anual} la recaudación final obtenida , el objetivo anual de recaudación no se consiguió.")





datos_socios = []


opcion = 0 
while opcion != 8:
    print("---MENU---")
    print("1: Cargar datos de los socios")
    print("2: Mostrar los datos de los socios")
    print("3: Mostrar los legajos ordenados")
    print("4: Cambiar la condición del socio")
    print("5: Dar de baja un socio")
    print("6: Recaudación actual")
    print("7: Reecaudación mensual y anual")
    print("8: Salir")
    print("--------------------------------------")
    opcion = int(input("Ingrese una opción: "))
    while opcion < 1 or opcion > 8:
        print("Error, ingreso un valor no valido")
        opcion = int(input("Ingrese un valor del 1 al 8: "))
    if opcion == 1: 
        lista = cargaDeDatos()
        
        datos_socios.append(lista)
        DATOS = []
        for x in datos_socios:
            for y in x:
                DATOS.append(y)
        
    elif opcion == 2:
        mostrar_datos(DATOS)
        
    elif opcion == 3:
        legajos = 0
        for x in range (len(DATOS)):
            legajos += 1
        print(f"Hay {legajos} legajos guardados en el sistema")
        legajos_ordenados(DATOS)
    
    elif opcion == 4:
        cambiar_condicion(DATOS)

    elif opcion == 5:
        dar_baja(DATOS)

    elif opcion == 6:
        recaudacion_actual (DATOS)

    elif opcion == 7:
        recaudacion(DATOS)

    
