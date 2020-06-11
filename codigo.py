opcion = input("di un numero:")

while True:
    if opcion == "1":
        mensaje = input("Dime el mensaje que sedea guardar")
        archivo = open("archivo.txt",'w')
        archivo.write("mensaje")
        archivo.close()
    
    if opcion == "2":
        break