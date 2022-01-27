"""
una aplicacion
debe ser una aplicacion que pueda sumar cualquier cantidad de numeros y
luego dar la suma.

la aplicacion debe tener un menu presentado al usuario en consola y
debe tener las opciones de agregar un nuevo numero y mostrar
la suma de los numeros que se tienen
debe tener opcion para terminar el programa

 0:: agregar un nuevo numero
 1:: mostrar la suma
-1:: exit

"""
result = 0

while True:
    option = int(input("option: "))
    if option == -1:
        break
    elif option == 0:
        print("agregar numero...")
    elif option == 1:
        print(f"result-> {result}")
    else:
        print("app is working...")
