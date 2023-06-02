from usuario import Usuario
from administrador import Administrador

u = Usuario("joao", "joao@exemplo.com")
a = Administrador("Admin", "admin@exemplo.com")

u.imprime_usuario()
a.imprime_usuario()

print(Usuario.quantidade)
