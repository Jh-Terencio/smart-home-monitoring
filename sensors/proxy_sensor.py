# sensors/proxy_sensor.py

from patterns.observer import Sensor

class SensorProxy(Sensor):
    def __init__(self, real_sensor):
        # Armazena a instância do sensor real que o proxy está representando
        self._real_sensor = real_sensor
        self._cache = None  # Inicialmente, não há valor armazenado em cache

    def read_value(self):
        # Verifica se há um valor em cache; se não houver, lê o valor do sensor real
        if self._cache is None:
            self._cache = self._real_sensor.read_value()
        return self._cache  # Retorna o valor em cache

    def invalidate_cache(self):
        # Invalida o cache para que o próximo acesso faça uma nova leitura
        self._cache = None

    def apply_climate_event(self, effect):
        # Delegar a chamada de apply_climate_event para o sensor real
        if hasattr(self._real_sensor, 'apply_climate_event'):
            self._real_sensor.apply_climate_event(effect)
