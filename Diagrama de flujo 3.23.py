############
#Elaborado por: Daniel Campos
#Fecha de creación: 18-08-2023 6:10pm
#Última modificación: 19-08-2023 4:08pm
#Versión: 3.10.6
############
tipo1=0
tipo2=0
tipo3=0
tipo4=0
tipo5=0
#tipos de vinos
mctipo2=0
#cantidad de vino producido en el mejor año
i=1
#contador 1
n=int(input("Digite los años en los que se desea hacer el cálculo: "))
while i<=n:
    j=1
    #contador 2
    totvin=0
    #vinos producidos anualmente
    while j<=5:
        v=int(input("Cantidad de litros de vino "+str(j) + " producido en el año "+str(i) + " : "))
        #contador de litros producidos de cada tipo de vino anualmente
        totvin+=v
        if j==1:
            tipo1+=v
        elif j==2:
            tipo2+=v
            if v>mctipo2:
                mctipo2=v
                anno=i
        elif j==3:
            tipo3+=v
            if v==0:
                print("El año ", i, " no ha producido vino tipo 3.")
        elif j==4:
            tipo4+=v
        else:
            tipo5+=v
        j+=1
    else: 
        print("\n", "Total litros producidos en el año ", i, ": ", totvin, "\n")
        i+=1
else:
    if n>0:
        print("\n", "Total Tipo 1: ", tipo1, "\n", "Total Tipo 2: ", tipo2, "\n", "Total Tipo 3: ", tipo3, "\n", "Total Tipo 4: ", tipo4, "\n", "Total Tipo 5: ", tipo5)
        print("\n","Año en que se produjo mayor cantidad de vino tipo 2:", "\n", "Año: ", anno, "\n" " Litros: ", mctipo2)
    else:
        print("Se necesita una cantidad de años definida para hacer el cálculo.")
        #por si n=0 (0 años)