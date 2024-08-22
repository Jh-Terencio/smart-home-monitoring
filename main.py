# main.py

# Importa o MessageBroker
from broker.message_broker import MessageBroker

# Importa os sensores
from sensors.temperature_sensor import TemperatureSensor
from sensors.humidity_sensor import HumiditySensor
from sensors.motion_sensor import MotionSensor
from sensors.presence_sensor import PresenceSensor
from sensors.proxy_sensor import SensorProxy  # Proxy para controlar o acesso aos sensores

# Importa os dispositivos
from devices.alarm import Alarm
from devices.light_control import LightControl
from devices.thermostat import Thermostat
from devices.sprinkler import Sprinkler  # Novo dispositivo

# Importa a simulação de eventos climáticos
from climate_event import ClimateEvent

# Função principal que executa a simulação do sistema de monitoramento residencial
def main():
    # Cria a instância do MessageBroker (Singleton)
    broker = MessageBroker()

    # Instancia os sensores
    temp_sensor = TemperatureSensor()
    hum_sensor = HumiditySensor()
    motion_sensor = MotionSensor()
    presence_sensor = PresenceSensor()

    # Cria proxies para os sensores (opcional, para simular cache ou acesso controlado)
    proxy_temp_sensor = SensorProxy(temp_sensor)
    proxy_hum_sensor = SensorProxy(hum_sensor)

    # Instancia os dispositivos
    alarm = Alarm()
    light_control = LightControl()
    thermostat = Thermostat()  # Instância do termostato
    sprinkler = Sprinkler()  # Novo dispositivo

    # Configura as assinaturas de dispositivos nos tópicos do broker
    broker.subscribe("motion", light_control)
    broker.subscribe("intrusion", alarm)
    broker.subscribe("temperature", thermostat)

    # Sprinkler responde a mudanças de temperatura e umidade
    broker.subscribe("climate", sprinkler)

    # Simulação de eventos climáticos
    climate = ClimateEvent()
    event_effects = climate.trigger_event()
    print(f"Evento climático: {climate.describe_event()}")

    # Aplica os efeitos climáticos nos sensores
    proxy_temp_sensor.apply_climate_event(event_effects["temperature_change"])
    proxy_hum_sensor.apply_climate_event(event_effects["humidity_change"])

    # Simulação de leituras e publicações no broker
    print("\n### Simulação de Leitura dos Sensores ###\n")

    # Temperatura e umidade simuladas
    temperature = proxy_temp_sensor.read_value()
    humidity = proxy_hum_sensor.read_value()
    print(f"Temperatura lida: {round(temperature,2)}°C, Umidade lida: {round(humidity,2)}%")

    # Ajuste automático do modo do termostato baseado na temperatura
    if temperature > 30:
        thermostat.set_mode("cool")
    elif temperature < 18:
        thermostat.set_mode("heat")
    else:
        thermostat.set_mode("off")

    # Publica o clima para o Sprinkler
    broker.publish("climate", {"temperature": temperature, "humidity": humidity})

    # Leitura de movimento e publicação no broker
    motion_detected = motion_sensor.read_value()
    print(f"Movimento detectado: {motion_detected}")
    broker.publish("motion", "MOTION_DETECTED" if motion_detected else "NO_MOTION")

    # Leitura de presença e publicação no broker
    presence_detected = presence_sensor.read_value()
    print(f"Presença detectada: {presence_detected}")
    broker.publish("intrusion", "INTRUDER_DETECTED" if presence_detected else "NO_INTRUDER")

if __name__ == "__main__":
    main()
