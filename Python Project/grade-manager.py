

calificaciones=[]
nombres=[]

terminado=False


def agregar(calificacion, nombre):
    calificaciones.append(int(calificacion))
    nombres.append(nombre)                

def promedio():
    if not calificaciones:
        print("No hay calificaciones para calcular el promedio.")
        return
    promedio = sum(calificaciones) / len(calificaciones)
    print(f'Tu promedio es: {promedio:.2f}%')

def ver():
    print('tus calificaciones son:')
    for c in range(len(calificaciones)):
        print(f'calificacion numero:{c+1} es {calificaciones[c]}% y el nombre:{nombres[c]}')

def borrar(numero):
    if 1 <= numero <= len(calificaciones):
        del calificaciones[numero - 1]
        del nombres[numero - 1]
        print("¡Elemento borrado!")
    else:
        print("Número inválido, intenta otra vez.")

while not terminado:
    print('OBCIONES:')
    print('1 agregar calificacion')
    print('2 calcular promedio')
    print('3 ver calificaciones')
    print('4 borrar calificacion')
    desicion=int(input())
    if desicion == 1:
        nombre = input("dime el nombre: ")
        calificacion = int(float(input("dime la calificacion: ")))
        agregar(calificacion, nombre)
        print('listo!!!')
    elif desicion == 2:
        promedio()
    elif desicion == 3:
        if not calificaciones:
            print("pon algo en la lista")
        else:
            ver()
    elif desicion == 4:
        if not calificaciones:
            print("No hay calificaciones para borrar.")
        else:
            ver()
            Dborrar = int(input("¿Cuál quieres borrar? "))
            borrar(Dborrar)
