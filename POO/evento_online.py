# Importação de módulo
from evento import Evento

# Herança -> classe EventoOnline herda da classe mãe Evento
class EventoOnline(Evento):
    def __init__(self, nome, _=""): # _ significa que o parametro será ignorado
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
        super().__init__(nome, local) # referencia a classe mãe, por isso não necessita do self
    
    def imprime_informacoes(self):
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Link para acessar o evento: {self.local}")
        print("-----------------------")