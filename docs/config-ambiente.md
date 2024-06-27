# Manual de configuração do ambiente
 
## 1 - Criando Venv
 
Com o `cmd` na pasta, digite o seguinte comando para criar um `ambiente virtual` (venv), em seguida aperte ENTER:
```
py -m venv venv
```

### 2 - Ativando venv via cmd
 
Para ativar o `ambiente virtual` criado via `cmd`, basta digitar o seguinte comando e em seguida apertar ENTER:
```
venv\Scripts\activate
```
 
### 3 - Instalando dependências
 
Para instalar as dependências que o sistema precisa para funcionar corretamente, basta digitar o seguinte comando no `cmd` e em seguida apertar ENTER:
 
```
python -m pip install -r requirements.txt
```
 
### 4 - Atualizando o pip
 
Para atualizar o pip no `ambiente virtual`, primeiro certifique-se de que o ambiente está ativo, lembre-se da sinalização mostrada na ativação do venv, em seguida digite o seguinte comando e aperte ENTER:
```
python -m pip install --upgrade pip
```