# sensors/__init__.py

# Este arquivo serve para definir o diretório 'sensors' como um pacote Python,
# permitindo que seus módulos (os diferentes tipos de sensores) sejam importados.

# Exemplo de importações que podem ser feitas automaticamente quando o pacote é importado
from .temperature_sensor import TemperatureSensor
from .humidity_sensor import HumiditySensor
from .motion_sensor import MotionSensor
from .presence_sensor import PresenceSensor

# Define quais sensores serão acessíveis ao importar o pacote 'sensors' diretamente.
__all__ = ['TemperatureSensor', 'HumiditySensor', 'MotionSensor', 'PresenceSensor']