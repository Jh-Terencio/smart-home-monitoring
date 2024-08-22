# devices/alarm.py

from patterns.observer import Device

class Alarm(Device):
    def __init__(self):
        self.silent_mode = False  # Modo silencioso ativado ou não

    def set_silent_mode(self, silent):
        """
        Define se o alarme está no modo silencioso.
        """
        self.silent_mode = silent

    def update(self, data):
        """
        O método update será chamado quando houver uma nova publicação no tópico "intrusion".
        """
        if data == "INTRUDER_DETECTED":
            if self.silent_mode:
                print("Modo silencioso: Intruso detectado. Notificação enviada!")
            else:
                print("Alarme disparado: Intruso detectado!")
        else:
            print("Nenhum intruso detectado.")
