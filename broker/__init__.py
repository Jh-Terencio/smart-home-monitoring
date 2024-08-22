# broker/__init__.py

# Este arquivo define o diretório 'broker' como um pacote Python,
# permitindo que seu conteúdo seja importado a partir de outros módulos.

# Exemplo de importação que pode ser feita automaticamente ao importar o pacote 'broker'
from .message_broker import MessageBroker

# Define que ao importar 'broker', o objeto 'MessageBroker' estará disponível.
__all__ = ['MessageBroker']