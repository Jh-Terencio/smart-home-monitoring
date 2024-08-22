# sensors/temperature_sensor.py

import random
import math
from patterns.observer import Sensor

class TemperatureSensor(Sensor):
    def __init__(self):
        self.base_temperature = 25.0  # Temperatura base
        self.time_of_day = 12.0       # Simula o tempo do dia
        self.amplitude = 10.0         # Amplitude para variação de temperatura
        self.climate_effect = 0.0     # Efeito climático na temperatura

    def apply_climate_event(self, temperature_change):
        """
        Aplica o efeito de um evento climático na temperatura.
        """
        self.climate_effect = temperature_change

    def generate_temperature(self):
        """
        Gera a temperatura com base na hora do dia e condições climáticas.
        """
        # Usamos uma distribuição normal para gerar variações realistas
        base_temp = random.gauss(self.base_temperature, 2.0)  # Distribuição normal centrada na base
        
        # Variação ao longo do dia (usando função seno para simular o ciclo de 24 horas)
        daily_variation = self.amplitude * math.sin((self.time_of_day / 24.0) * 2 * math.pi)
        
        # A variação climática será somada ao resultado
        return base_temp + daily_variation + self.climate_effect

    def read_value(self):
        """
        Lê o valor da temperatura simulando variações baseadas em cenários reais.
        """
        self.time_of_day = (self.time_of_day + random.uniform(0.1, 0.5)) % 24
        
        # Gera uma nova temperatura
        self.temperature = self.generate_temperature()

        # Mantém a temperatura dentro de intervalos realistas
        if self.temperature > 35:
            print("Temperatura muito quente!")
        elif 30 <= self.temperature <= 35:
            print("Temperatura alta!")
        elif 23 <= self.temperature < 30:
            print("Temperatura normal.")
        else:
            print("Temperatura baixa!")

        return self.temperature
