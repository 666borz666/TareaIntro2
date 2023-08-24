############
#Elaborado por: Daniel Campos
#Fecha de creación: 18-08-2023 4:00pm
#Última modificación: 18-08-2023 6:01pm
#Versión: 3.10.6
############
arsu=0
arno=0
arce=0
#lluvia caida en las regiones
mersu=50000
i=1
while i<=12:
    rno=int(input("Lluvia caída en la región norte del mes "+str(i)+ " :"))
    rce=int(input("Lluvia caída en la región central del mes "+str(i)+ " :"))
    rsu=int(input("Lluvia caída en la región sur del mes "+str(i)+ " :"))
    #cantidad de lluvia en los 12 meses
    arno+=rno
    arce+=rce
    arsu+=rsu
    #cambia los datos de las variables iniciadas en 0
    if mersu>rsu:
        mersu=rsu
        mes=1
        #registro del mes, lluvia sur
    i+=1
else:
    prorce=arce/12
    #se divide entre 12 para el promedio
    print("Promedio región centro:", prorce, "\n" "Mes con menor lluvia en el sur:", mes, "\n" "Registro del mes con menor lluvia en el sur:", mersu)
    #datos procesados anteriormente
    if arno>arce:
        if arno>arsu:
            print("La región con mayor lluvia es la norte")
        else:
            print("La región con mayor lluvia es la sur")
    else:
        if arce>arsu:
            print("La región con mayor lluvia es la central")
        else:
            print("La región con mayor lluvia es la sur")
    #región con más lluvia anual