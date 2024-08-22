# devices/light_control.py

from patterns.observer import Device

class LightControl(Device):
    def __init__(self):
        self.auto_mode = True  # Modo automático ativado por padrão

    def set_auto_mode(self, auto):
        """
        Define se o controle de luz está no modo automático ou manual.
        """
        self.auto_mode = auto

    def manual_control(self, turn_on):
        """
        Controla a luz manualmente (ativar/desativar).
        """
        if turn_on:
            print("Luz manualmente ligada.")
        else:
            print("Luz manualmente desligada.")

    def update(self, data):
        """
        O método update será chamado quando houver uma nova publicação no tópico "motion".
        Se estiver em modo automático, a luz responderá ao movimento.
        """
        if self.auto_mode:
            if data == "MOTION_DETECTED":
                print("Luz acesa automaticamente por movimento!")
            else:
                print("Luz desligada.")
        else:
            print("Modo manual: luz não responde ao movimento.")
