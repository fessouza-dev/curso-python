class Evento:
    id = 1
    dia = 10
    
    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id # a instancia inicializada recebe o valor id da classe Evento -> self.id atributo de instancia
        Evento.id += 1 # Evento.id atributo de classe
    
    def imprime_informacoes(self):
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Local do evento: {self.local}")
        print("-----------------------")
    
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
        
# Herança -> classe EventoOnline herda da classe mãe Evento
class EventoOnline(Evento):
    def __init__(self, nome, _=""): # _ significa que o parametro será ignorado
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
        super().__init__(self, nome, local) # referencia a classe mãe
    
    def imprime_informacoes(self):
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Link para acessar o evento: {self.local}")
        print("-----------------------")
        
        
ev = Evento("Aula de Python")
ev.imprime_informacoes()

ev2 = Evento("Aula de JavaScript", "Rio de Janeiro")
ev2.imprime_informacoes()

ev_online = EventoOnline("Live de Python")
ev_online.imprime_informacoes()

ev2_online = EventoOnline("Live de JavaScript")
ev2_online.imprime_informacoes()

print(ev_online.dia)