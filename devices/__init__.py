# devices/__init__.py

# Este arquivo define o diretório 'devices' como um pacote Python,
# permitindo que seus módulos (os diferentes tipos de dispositivos) sejam importados.

# Exemplo de importações que podem ser feitas automaticamente quando o pacote é importado
from .alarm import Alarm
from .light_control import LightControl
from .thermostat import Thermostat

# Define quais dispositivos estarão disponíveis ao importar o pacote 'devices' diretamente.
__all__ = ['Alarm', 'LightControl', 'Thermostat']