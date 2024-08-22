# patterns/__init__.py

# Este arquivo define o diretório 'patterns' como um pacote Python,
# permitindo que seus módulos (os padrões de design) sejam importados.

# Importação automática dos padrões Observer e Singleton
from .observer import Sensor, Device
from .singleton import Singleton

# Define que ao importar 'patterns', as classes Sensor, Device e Singleton estarão disponíveis.
__all__ = ['Sensor', 'Device', 'Singleton']