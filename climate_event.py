# climate_event.py

import random

class ClimateEvent:
    def __init__(self):
        # Inicializa o estado atual do clima
        self.current_event = None

    def trigger_event(self):
        """
        Simula a ocorrência de um evento climático.
        Retorna um dicionário com as alterações para temperatura e umidade.
        """
        # Probabilidade de ocorrência de diferentes eventos
        event_probability = random.random()

        if event_probability < 0.2:
            # Simula um dia quente e seco
            self.current_event = "Hot and Dry Day"
            return {"temperature_change": random.uniform(5.0, 10.0), "humidity_change": random.uniform(-10.0, -5.0)}
        elif event_probability < 0.4:
            # Simula um dia frio e úmido
            self.current_event = "Cold and Humid Day"
            return {"temperature_change": random.uniform(-10.0, -5.0), "humidity_change": random.uniform(5.0, 10.0)}
        elif event_probability < 0.6:
            # Simula uma mudança rápida de clima
            self.current_event = "Rapid Climate Change"
            return {"temperature_change": random.uniform(-5.0, 5.0), "humidity_change": random.uniform(-5.0, 5.0)}
        else:
            # Nenhuma mudança climática significativa
            self.current_event = "Normal Day"
            return {"temperature_change": 0.0, "humidity_change": 0.0}

    def describe_event(self):
        """
        Descreve o evento climático atual.
        """
        return self.current_event if self.current_event else "No Event"