# broker/message_broker.py

# Implementação de um Message Broker usando o padrão Singleton.

class MessageBroker:
    _instance = None  # Atributo de classe para armazenar a instância Singleton.
    
    def __new__(cls):
        # Verifica se já existe uma instância do MessageBroker.
        if cls._instance is None:
            # Se não houver instância, cria uma nova.
            cls._instance = super(MessageBroker, cls).__new__(cls)
            # Inicializa um dicionário para armazenar os tópicos e seus subscribers.
            cls._topics = {}
        return cls._instance  # Retorna a instância (Singleton).

    def subscribe(self, topic, subscriber):
        """
        Permite que um dispositivo (subscriber) se inscreva em um tópico específico.
        :param topic: O nome do tópico (string) no qual o subscriber deseja se inscrever.
        :param subscriber: O dispositivo (objeto) que deseja receber atualizações.
        """
        # Se o tópico ainda não existir, cria uma lista vazia para ele.
        if topic not in self._topics:
            self._topics[topic] = []
        # Adiciona o subscriber à lista de dispositivos inscritos no tópico.
        self._topics[topic].append(subscriber)

    def publish(self, topic, data):
        """
        Publica dados em um tópico, notificando todos os subscribers inscritos nesse tópico.
        :param topic: O nome do tópico (string) no qual os dados serão publicados.
        :param data: Os dados que serão enviados para os subscribers.
        """
        # Verifica se o tópico existe e se há subscribers para ele.
        if topic in self._topics:
            # Itera sobre todos os subscribers inscritos no tópico.
            for subscriber in self._topics[topic]:
                # Notifica o subscriber chamando seu método 'update' e passando os dados.
                subscriber.update(data)