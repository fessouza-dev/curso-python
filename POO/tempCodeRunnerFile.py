class Evento:
    id = 1
    dia = 10
    
    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id # a instancia inicializada recebe o valor id da classe Evento -> self.id atributo de instancia
        Evento.id += 1 # Evento.id atributo de classe
    
    def imprime_informacoes(self):
        print("ID do evento:", self.id)
        print("Nome do evento:", self.nome)
        print("Local do evento:", self.local)
        print("-----------------------")
        
    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local="https://tamarcado.com/eventos?id={cls.id}") # interpolar
        return evento
    # Dentro desse método, uma nova instância da classe evento é criada usando o construtor da classe
    
    @staticmethod
    def calcula_limite_pessoas_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0
        
ev = Evento("Aula de Python")
ev.imprime_informacoes()

ev2 = Evento("Aula de JavaScript", "Rio de Janeiro")
ev2.imprime_informacoes()

ev_online = Evento.cria_evento_online("Live de Python")
ev_online.imprime_informacoes()

ev2_online = Evento.cria_evento_online("Live de JavaScript")
ev2_online.imprime_informacoes()

print(ev_online.dia)