import random
import string
caracteres = string.ascii_letters + string.digits + string.digits 
contraseña = ''.join(random.choice(caracteres)for i in range(12)) 
print("Contraseña Generada:", contraseña)