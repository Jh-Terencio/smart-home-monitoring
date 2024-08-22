
# sensors/presence_sensor.py

from patterns.observer import Sensor  # Importa a interface Sensor, que será implementada.

class PresenceSensor(Sensor):
    def __init__(self):
        # Inicialmente, o sensor não detecta a presença de uma pessoa.
        self.presence_detected = False

    def read_value(self):
        # Simula a detecção de presença (True ou False).
        import random
        self.presence_detected = random.choice([True, False])
        return self.presence_detected  # Retorna se há ou não presença.