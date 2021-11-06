masa=float(input("ingresa tu peso"))
altura=float(input("ingresa tu altura"))

imc = masa/altura**2 


print("tu inc es: "+ str(imc))

if imc>25:
    print("Tienes Sobrepeso")