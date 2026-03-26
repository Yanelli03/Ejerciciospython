#Crear una subrutina llamada "Login", que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es "usuario1" y la contraseña es "asdasd".

def login(usuario,clave,intentos):
    usuario_correcto = 'Noah'
    clave_correcta = 'Noahxd123'

    intentos += 1
    if usuario == usuario_correcto and clave == clave_correcta:
        return True,intentos
    else:
        return False,intentos
    
intentos = 0
entrar = False

while not entrar and intentos < 3:
        usuario = input('usuario: ')
        clave = input('password: ')

        entrar, intentos = login(usuario,clave,intentos)
        if not entrar:
            print('Error. Nombre de usuario o contraseña incorrecta.')

        if entrar:
            print('Bienvenido al sistema')
        else:
            print('No has entrado al sistema')