
# patterns/observer.py

from abc import ABC, abstractmethod  # Importa a biblioteca para criar classes abstratas.

# Interface abstrata para sensores (Publishers) no padrão Observer.
class Sensor(ABC):
    @abstractmethod
    def read_value(self):
        """
        Método abstrato que define a leitura de dados de um sensor.
        As classes derivadas precisam implementar este método.
        """
        pass

# Interface abstrata para dispositivos (Subscribers) no padrão Observer.
class Device(ABC):
    @abstractmethod
    def update(self, data):
        """
        Método abstrato que define como os dispositivos reagem a novos dados publicados.
        As classes derivadas precisam implementar este método.
        """
        pass