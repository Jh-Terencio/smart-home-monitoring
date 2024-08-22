from patterns.observer import Sensor  # Importa a interface Sensor, que será implementada.

class MotionSensor(Sensor):
    def __init__(self):
        # Inicialmente, o sensor não detecta movimento.
        self.motion_detected = False

    def read_value(self):
        # Simula a detecção ou não de movimento (True ou False).
        import random
        self.motion_detected = random.choice([True, False])
        return self.motion_detected  # Retorna o estado atual de movimento.
