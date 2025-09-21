# Actividad
- Algoritmo simple para romper contraseñas (fuerza bruta controlada)


First, import the time and itertools. After that the value of the password variable is assigned. As this is a simple example, only lowercase letters were used, and therefore a value is assigned to the alfabeto.
Intentos count the attempts made to find the password and tiempo_inicia save the time it took to find the password.
max_length is the length of combinations to be tested
Then we do a loop that runs through all combination lengths, from 1 to max_length. And we also have a counter. And we do a if and else loop.

At the end the program will show this:
 1. contraseña encontrada
 2. numero de intentos: 1067
 3. Tiempo de: 0.0005 segundos

The program evaluates all possible combinations to guess the password. Since this is a simple example, it takes very little time to find the password. However, in real life, longer passwords with high security are used, such as those containing numbers, capital letters, and characters, so it may take longer to find the password. 
