import requests

def MostrarMenu():

    print("==============Bienvenido a la APP Datos Random de los Gatos==============")
    print("=========================================================================")
    print("[1] Obtener dato aleatoreo extraño de los Gatos ")
    print("[2] Obtener todos los datos extraños de los Gatos ")
    print("[3] Eliminar dato extraño de los Gatos ")


MostrarMenu()
opcion = input("Seleccione una Opcion : ")

if opcion == "1":
    r = requests.get('https://catfact.ninja/fact')
    #guardar el dato en BD

    data = r.json()
    #Mostrar dato
    #print(r.json())
    print(data['fact'])
