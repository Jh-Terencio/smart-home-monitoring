# devices/sprinkler.py

from patterns.observer import Device

class Sprinkler(Device):
    def __init__(self):
        self.temperature_threshold = 30.0  # Temperatura mínima para ativar o sprinkler
        self.humidity_threshold = 40.0     # Umidade máxima para ativar o sprinkler
        self.is_on = False                 # Estado atual do sprinkler (ligado ou desligado)

    def update(self, data):
        """
        O método update será chamado quando houver uma nova leitura de temperatura e umidade.
        O sprinkler será ativado se as condições forem adequadas (muito quente e seco).
        """
        if isinstance(data, dict):
            temperature = data.get('temperature')
            humidity = data.get('humidity')

            if temperature is not None and humidity is not None:
                if temperature > self.temperature_threshold and humidity < self.humidity_threshold:
                    self.turn_on()
                else:
                    self.turn_off()

    def turn_on(self):
        if not self.is_on:
            print("Sprinkler ligado: molhando o jardim! Temperatura alta e umidade baixa.")
            self.is_on = True

    def turn_off(self):
        if self.is_on:
            print("Sprinkler desligado.")
            self.is_on = False
