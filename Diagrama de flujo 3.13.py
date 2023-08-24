############
#Elaborado por: Daniel Campos
#Fecha de creación: 18-08-2023 2:40pm
#Última modificación: 20-08-2023 5:06pm
#Versión: 3.10.6
############
men=100000
may=-100000
#valor máximo y mínimo a evaluar
n=int(input("Digite la cantidad de números a comparar: "))
i=0
#controlador de ciclo
while i<=(n-1):
    #resta de uno porque compararía 1 número más
    if n>=2:
        #para comparar se necesita 2 o más cosas
        num=int(input("Digite un número: "))
        if num>may:
            may=num
            #cambia la variable por el número dado
        if num<men:
            men=num
            #cambia la variable por el número dado
        i+=1
    else:     
        print("La cantidad mínima es de 2 números.") 
        i+=2
        #evita que imprima 2 veces lo mismo (se da cuando se digita 1)
else:
    if n>=2:
        print("Mayor: ",may,"Menor: ",men)
    else:
        print("")
        #evita la creación de un bucle