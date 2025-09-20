import itertools
import time

password = "wzm"

alfabeto = "abcdefghijklmnopqrstuvwxyz"

intentos = 0
tiempo_inicia = time.time()

found = False
max_length = 4  

for a in range(1, max_length + 1):
    
    for b in itertools.product(alfabeto, repeat=a):
        intentos += 1
        intento = "".join(b)
        if intento == password:
            found = True
            acaba_tiempo = time.time()
            break
    if found:
        break

if found:
    print(f"contraseña encontrada")
    print(f"numero de intentos: {intentos}")
    print(f"tiempo de: {acaba_tiempo - tiempo_inicia:.4f} segundos")
else:
    print(" Contraseña no encontrada")
