print("*** Generador de Email ***")
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese sus apellidos: ")
nombre_empresa = input("Ingrese el nombre de su empresa: ")
extension_dominio = input("Ingrese el dominio de su correo: ")

nombre_usuario = nombre_usuario.lower().strip().replace(" ", ".")
apellido_usuario = apellido_usuario.lower().strip().replace(" ", ".")
nombre_empresa = nombre_empresa.lower().strip().replace(" ", "")

print("\n*** Generador de Email ***")
print(f"Tu correo es:\n{nombre_usuario}.{apellido_usuario}@{nombre_empresa}{extension_dominio.strip()}")

