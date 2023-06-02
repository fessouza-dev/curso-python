class Usuario():
    quantidade = 0
    
    def __init__(self, nome, email):
        Usuario.quantidade += 1
        self.nome = nome
        self.email = email
        
    def imprime_usuario(self):
        print(f"{self.nome} ({self.email})")