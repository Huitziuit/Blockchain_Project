from hashlib import sha256 #Hashing usado en bitcoin 

transactions = ["User <Erick Huitziuit> init $10 HuitziCoins",
                "Uset <Adan Giovani> init $10 HuitziCoins"]


data = "_".join(transactions) # Unimos el contenido de la informacion sobre las transacciones para el bloque 

print("Transacciones del bloque: " + data)

transactions_hash = sha256(data.encode()).hexdigest()
#El método encode() se utiliza para convertir el objeto data en una secuencia de bytes utilizando una codificación 
# de caracteres. Esto es necesario para poder aplicar la función hash SHA-256, que opera en bytes en lugar de 
# cadenas de caracteres, el resultado es un objeto de tipo hash que con la funcion .hexdigest() pasa de su forma binaria
# a caracteres hexadecimales 

print("Clave hash de la data: "+ transactions_hash)
