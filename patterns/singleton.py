# patterns/singleton.py

# Implementação genérica do padrão Singleton
class Singleton:
    _instances = {}  # Dicionário que armazena as instâncias criadas.

    def __new__(cls, *args, **kwargs):
        """
        Método especial que controla a criação de instâncias da classe.
        Garante que apenas uma instância da classe seja criada.
        """
        # Verifica se já existe uma instância da classe.
        if cls not in cls._instances:
            # Se não existir, cria uma nova instância e a armazena no dicionário.
            cls._instances[cls] = super(Singleton, cls).__new__(cls)
        # Retorna a instância existente ou recém-criada.
        return cls._instances[cls]