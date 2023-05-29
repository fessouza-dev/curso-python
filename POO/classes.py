class Evento:
    def __init__(self, nome):
        """
        Construtor da classe Evento.
        Inicializa o objeto
        """
        self.nome = nome
        
    def altera_nome_evento(self, novo_nome): 
        print("Alterando nome do evento")
        self.nome = novo_nome
        """
        self define que todo método da classe que for chamado
        por um obj, o primeiro parametro é a referência ao próprio obj
        
        Em java, this.nome funciona também como forma de 
        referenciar ao objeto que está chamando o método da classe
        """
        
    
# obj criado a partir de uma certa classe se chama instancia
ev = Evento("Aula de Python")
print(ev.nome)

ev2 = Evento("Aula de JavaScript")
print(ev2.nome)

"""
ev.altera_nome_evento(ev, "Aula de JavaScript") é o mesmo que
ev.altera_nome_evento(ev, ev, "Aula de JavaScript") -> primeiro parametro é o obj que chamou o método
"""
ev.altera_nome_evento("Aula de JavaScript")
print(ev.nome)

ev2.altera_nome_evento("Aula de Python")
print(ev2.nome)
