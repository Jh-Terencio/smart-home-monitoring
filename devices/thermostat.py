# devices/thermostat.py

from patterns.observer import Device

class Thermostat(Device):
    def __init__(self):
        self.target_temperature = 22.0  # Temperatura desejada
        self.mode = "off"  # Modos: off, heat, cool

    def set_mode(self, mode):
        """
        Define o modo do termostato (off, heat, cool).
        """
        if mode in ["off", "heat", "cool"]:
            self.mode = mode
            print(f"Termostato ajustado para o modo: {mode}.")
        else:
            print("Modo inválido. Escolha entre 'off', 'heat', ou 'cool'.")

    def update(self, data):
        """
        O método update será chamado quando houver uma nova leitura de temperatura.
        Reage de acordo com o modo definido.
        """
        if isinstance(data, (int, float)):
            current_temperature = data
            if self.mode == "heat" and current_temperature < self.target_temperature:
                print(f"Aquecendo ambiente. Temperatura atual: {current_temperature}°C.")
            elif self.mode == "cool" and current_temperature > self.target_temperature:
                print(f"Resfriando ambiente. Temperatura atual: {current_temperature}°C.")
            elif self.mode == "off":
                print("Termostato desligado.")
            else:
                print(f"Temperatura ideal mantida em {self.target_temperature}°C.")
