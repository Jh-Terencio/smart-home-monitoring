# sensors/humidity_sensor.py

import random
import math
from patterns.observer import Sensor

class HumiditySensor(Sensor):
    def __init__(self):
        self.base_humidity = 50.0  # Umidade base
        self.time_of_day = 12.0    # Simula o tempo do dia
        self.amplitude = 20.0      # Amplitude de variação da umidade
        self.climate_effect = 0.0  # Efeito climático na umidade

    def apply_climate_event(self, humidity_change):
        """
        Aplica o efeito de um evento climático na umidade.
        """
        self.climate_effect = humidity_change

    def generate_humidity(self):
        """
        Gera a umidade com base na hora do dia e condições climáticas.
        """
        # Usamos uma distribuição normal para gerar variações realistas
        base_humidity = random.gauss(self.base_humidity, 5.0)  # Distribuição normal centrada na base

        # Variação ao longo do dia (usando função seno para simular o ciclo de 24 horas)
        daily_variation = self.amplitude * math.sin((self.time_of_day / 24.0) * 2 * math.pi)

        # A variação climática será somada ao resultado
        return base_humidity + daily_variation + self.climate_effect

    def read_value(self):
        """
        Lê o valor da umidade simulando variações baseadas em cenários reais.
        """
        self.time_of_day = (self.time_of_day + random.uniform(0.1, 0.5)) % 24

        # Gera uma nova umidade
        self.humidity = self.generate_humidity()

        # Mantém a umidade dentro de intervalos realistas
        if self.humidity < 30:
            print("Umidade muito baixa (ar seco)!")
        elif self.humidity < 40:
            print("Umidade baixa.")
        elif self.humidity > 70:
            print("Umidade alta!")
        else:
            print("Umidade normal.")

        return self.humidity
