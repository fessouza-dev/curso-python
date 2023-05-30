# Importação de módulo
from evento import Evento
from evento_online import EventoOnline
        
ev = Evento("Aula de Python")
ev.imprime_informacoes()

ev2 = Evento("Aula de JavaScript", "Rio de Janeiro")
ev2.imprime_informacoes()

ev_online = EventoOnline("Live de Python")
# ev_online.imprime_informacoes()
print(ev_online.to_json())

ev2_online = EventoOnline("Live de JavaScript")
# ev2_online.imprime_informacoes()
print(ev2_online.to_json())
