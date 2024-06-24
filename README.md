# Sistema de Monitoramento Residencial Inteligente com Arquitetura Publish-Subscribe (IoT)

## Descrição do Projeto

Este projeto visa desenvolver um sistema de monitoramento residencial inteligente usando a arquitetura publish-subscribe para integrar dispositivos IoT em uma rede doméstica. Monitora temperatura, umidade, luminosidade, movimento e presença de pessoas com sensores reais ou simulados.

## Funcionalidades Principais

- **Integração de Sensores IoT:** Utilização ou simulação de sensores para monitorar diferentes aspectos da casa.
- **Arquitetura Publish-Subscribe:** Implementação de um barramento de mensagens onde os sensores publicam dados em tópicos específicos.
- **Subscrição de Dispositivos:** Dispositivos inscritos nos tópicos recebem atualizações e respondem conforme necessário.
- **Automação Residencial:** Exploração de cenários como automação de iluminação, disparo de alarmes, controle automático de temperatura, entre outros.
- **Utilização de Message Brokers:** Implementação utilizando Message Broker (ex.: MQTT) e/ou websockets para comunicação eficiente.

## Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Message Broker:** MQTT (utilizando bibliotecas como `paho-mqtt`)
- **Frameworks Web:** Flask ou FastAPI
- **Hardware:** Raspberry Pi, sensores de temperatura, umidade, luminosidade, etc.

## Estrutura do Projeto

- `docs/`: Documentação detalhada do projeto.
- `src/`: Código fonte do projeto.
  - `sensors/`: Implementação dos sensores.
  - `broker/`: Configuração e implementação do Message Broker.
  - `web/`: Backend e frontend do sistema.
- `tests/`: Testes unitários e de integração.
- `scripts/`: Scripts auxiliares para configuração e automação.

## Instruções de Instalação

1. Clone o repositório:
   ```bash
   https://github.com/Jh-Terencio/smart-home-monitoring.git
