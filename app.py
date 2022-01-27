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
 2:: mostrar lista de numeros
-1:: exit

"""

from db import db


def showMenu():
    print()
    print()
    optionDict = {
        " 0": "agregar un nuevo numero",
        " 1": "mostrar la suma",
        " 2": "mostrar la lista de numeros",
        "-1": "exit",
    }
    for option, value in optionDict.items():
        print(f"{option}:: {value}")
    print()


def showResult(database):
    result = 0
    showNumberList()
    for number in database:
        result += number
    print(f"result-> {result}")


def inputNumber():
    print()
    number = int(input("positive number: "))
    db.append(number)
    showNumberList()


def showNumberList():
    print()
    print(f"list-> {db}")


while True:
    showMenu()
    option = int(input("option: "))
    if option == -1:
        break
    elif option == 0:
        inputNumber()
    elif option == 1:
        showResult(db)
        break
    elif option == 2:
        showNumberList()
    else:
        print("app is working...")
